import re
from typing import List, Dict, Tuple

class AIPositionDetector:
    def __init__(self):
        # 定义关键词模式
        self.signature_keywords = [
            r'签字', r'签名', r'签署', r'盖章', r'印章',
            r'甲方', r'乙方', r'丙方', r'签约方',
            r'法定代表人', r'授权代表', r'代表人',
            r'日期', r'年.*月.*日',
            r'单位.*章', r'公司.*章'
        ]
        
        # 定义位置权重
        self.position_weights = {
            'bottom_right': 3.0,  # 右下角权重最高
            'bottom_left': 2.5,
            'middle_right': 2.0,
            'middle_left': 1.5,
            'top_right': 1.0,
            'top_left': 0.5
        }
    
    def detect_stamp_positions(self, text_data: List[Dict]) -> List[Dict]:
        """
        基于文本内容和位置检测建议的盖章位置
        
        Args:
            text_data: PDF文本提取数据
            
        Returns:
            建议的盖章位置列表
        """
        suggested_positions = []
        
        for page_data in text_data:
            page_num = page_data['page']
            page_width = page_data['width']
            page_height = page_data['height']
            text_blocks = page_data['text_blocks']
            
            # 查找关键词位置
            keyword_positions = self._find_keyword_positions(text_blocks, page_width, page_height)
            
            # 分析页面布局
            layout_positions = self._analyze_page_layout(text_blocks, page_width, page_height)
            
            # 合并和评分
            page_positions = self._merge_and_score_positions(
                keyword_positions, layout_positions, page_width, page_height
            )
            
            # 为每个位置添加页面信息
            for pos in page_positions:
                pos['page'] = page_num
                suggested_positions.append(pos)
        
        # 按分数排序，返回前3个最佳位置
        suggested_positions.sort(key=lambda x: x['score'], reverse=True)
        return suggested_positions[:1]
    
    def _find_keyword_positions(self, text_blocks: List[Dict], page_width: float, page_height: float) -> List[Dict]:
        """查找关键词相关的位置，'盖章'优先且分数最高"""
        keyword_positions = []
        for block in text_blocks:
            text = block['text'].strip()
            bbox = block['bbox']  # [x0, y0, x1, y1]

            # 优先查找“盖章”
            if re.search(r'盖章', text):
                x = bbox[2] + 20
                y = bbox[1] - 10
                if x + 80 > page_width:
                    x = bbox[0] - 100
                if y < 0:
                    y = bbox[3] + 10
                position = {
                    'x': max(0, x),
                    'y': max(0, y),
                    'width': 80,
                    'height': 80,
                    'score': 10.0,  # 最高分
                    'reason': f'关键词优先匹配: {text[:20]}...'
                }
                keyword_positions.append(position)
                # 如果只要第一个“盖章”就返回，可加break
                # break

            # 其它关键词
            else:
                for keyword_pattern in self.signature_keywords[1:]:
                    if re.search(keyword_pattern, text):
                        x = bbox[2] + 20
                        y = bbox[1] - 10
                        if x + 80 > page_width:
                            x = bbox[0] - 100
                        if y < 0:
                            y = bbox[3] + 10
                        position = {
                            'x': max(0, x),
                            'y': max(0, y),
                            'width': 80,
                            'height': 80,
                            'score': 2.0,
                            'reason': f'关键词匹配: {text[:20]}...'
                        }
                        keyword_positions.append(position)
        return keyword_positions
    
    def _analyze_page_layout(self, text_blocks: List[Dict], page_width: float, page_height: float) -> List[Dict]:
        """分析页面布局，找出可能的签名区域"""
        layout_positions = []
        
        # 将页面分为9个区域
        regions = self._divide_page_regions(page_width, page_height)
        
        # 计算每个区域的文本密度
        region_densities = self._calculate_region_densities(text_blocks, regions)
        
        # 找出文本密度较低的区域作为候选位置
        for region_name, region_rect in regions.items():
            density = region_densities.get(region_name, 0)
            
            # 文本密度低的区域更适合盖章
            if density < 0.3:  # 阈值可调整
                weight = self.position_weights.get(region_name, 1.0)
                score = weight * (1 - density)  # 密度越低分数越高
                
                # 在区域中心放置印章
                center_x = (region_rect[0] + region_rect[2]) / 2 - 40
                center_y = (region_rect[1] + region_rect[3]) / 2 - 40
                
                position = {
                    'x': center_x,
                    'y': center_y,
                    'width': 80,
                    'height': 80,
                    'score': score,
                    'reason': f'布局分析: {region_name}区域'
                }
                layout_positions.append(position)
        
        return layout_positions
    
    def _divide_page_regions(self, page_width: float, page_height: float) -> Dict[str, Tuple[float, float, float, float]]:
        """将页面分为9个区域"""
        w_third = page_width / 3
        h_third = page_height / 3
        
        regions = {
            'top_left': (0, 0, w_third, h_third),
            'top_middle': (w_third, 0, 2 * w_third, h_third),
            'top_right': (2 * w_third, 0, page_width, h_third),
            'middle_left': (0, h_third, w_third, 2 * h_third),
            'middle_middle': (w_third, h_third, 2 * w_third, 2 * h_third),
            'middle_right': (2 * w_third, h_third, page_width, 2 * h_third),
            'bottom_left': (0, 2 * h_third, w_third, page_height),
            'bottom_middle': (w_third, 2 * h_third, 2 * w_third, page_height),
            'bottom_right': (2 * w_third, 2 * h_third, page_width, page_height)
        }
        
        return regions
    
    def _calculate_region_densities(self, text_blocks: List[Dict], regions: Dict) -> Dict[str, float]:
        """计算每个区域的文本密度"""
        region_densities = {}
        
        for region_name, region_rect in regions.items():
            region_area = (region_rect[2] - region_rect[0]) * (region_rect[3] - region_rect[1])
            text_area = 0
            
            for block in text_blocks:
                bbox = block['bbox']
                
                # 计算文本块与区域的重叠面积
                overlap = self._calculate_overlap(bbox, region_rect)
                text_area += overlap
            
            density = text_area / region_area if region_area > 0 else 0
            region_densities[region_name] = density
        
        return region_densities
    
    def _calculate_overlap(self, bbox1: Tuple[float, float, float, float], 
                          bbox2: Tuple[float, float, float, float]) -> float:
        """计算两个矩形的重叠面积"""
        x1 = max(bbox1[0], bbox2[0])
        y1 = max(bbox1[1], bbox2[1])
        x2 = min(bbox1[2], bbox2[2])
        y2 = min(bbox1[3], bbox2[3])
        
        if x2 > x1 and y2 > y1:
            return (x2 - x1) * (y2 - y1)
        return 0
    
    def _merge_and_score_positions(self, keyword_positions: List[Dict], 
                                 layout_positions: List[Dict],
                                 page_width: float, page_height: float) -> List[Dict]:
        """合并关键词位置和布局位置，并重新评分"""
        all_positions = keyword_positions + layout_positions
        
        # 去重：合并距离很近的位置
        merged_positions = []
        merge_threshold = 50  # 像素
        
        for pos in all_positions:
            merged = False
            for existing_pos in merged_positions:
                distance = ((pos['x'] - existing_pos['x']) ** 2 + 
                           (pos['y'] - existing_pos['y']) ** 2) ** 0.5
                
                if distance < merge_threshold:
                    # 合并位置，取较高分数
                    if pos['score'] > existing_pos['score']:
                        existing_pos.update(pos)
                    merged = True
                    break
            
            if not merged:
                merged_positions.append(pos)
        
        # 添加默认位置（如果没有找到合适位置）
        if not merged_positions:
            default_positions = [
                {
                    'x': page_width * 0.7,
                    'y': page_height * 0.8,
                    'width': 80,
                    'height': 80,
                    'score': 1.0,
                    'reason': '默认位置: 右下角'
                }
            ]
            merged_positions.extend(default_positions)
        
        return merged_positions

