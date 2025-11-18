import re

def extract_after_zero(s: str):

    # 检查字符串中是否包含"content"
    if "content" in s:
        # 首先找到 "0:" 的位置
        zero_pos = s.find("0:")
        if zero_pos == -1:
            return s  # 如果没有找到 "0:"，返回原始字符串
        
        # 从 "0:" 位置开始截取后面的子字符串
        substring = s[zero_pos:]
        
        # 在子字符串中找到第一个引号的位置
        quote_start = substring.find('"')
        if quote_start == -1:
            # 尝试查找单引号
            quote_start = substring.find("'")
            if quote_start == -1:
                return s  # 如果没有找到引号，返回原始字符串
            
            # 从第一个单引号后开始找第二个单引号
            quote_end = substring.find("'", quote_start + 1)
            if quote_end == -1:
                return s  # 如果没有找到第二个引号，返回原始字符串
        else:
            # 从第一个双引号后开始找第二个双引号
            quote_end = substring.find('"', quote_start + 1)
            if quote_end == -1:
                return s  # 如果没有找到第二个引号，返回原始字符串
        
        # 返回两个引号之间的内容
        return substring[quote_start + 1:quote_end]
    else:
        # 如果字符串中不包含"content"，直接返回原始字符串
        return s

# 示例
if __name__ == "__main__":
    s = """{
            content: {
                0: "112233"
            }
        }"""
    print(extract_after_zero(s))  # 输出：112233