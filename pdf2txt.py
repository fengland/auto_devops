import sys
import PyPDF2
import os



# 将 PDF 文件转换为 TXT 文件
# 使用 PyPDF2 库提取文本
# 输入：PDF 文件路径 和 输出 TXT 文件路径
# 输出：TXT 文件
# 注意：如果输入文件不存在，则输出错误信息
# 注意：如果输入文件存在，则输出处理完成信息
# 注意：如果输出文件存在，则覆盖输出文件
# 注意：如果输出文件不存在，则创建输出文件


def save_pdf_to_txt(pdf_path, txt_path):
    # 检查输入文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误：找不到文件 {pdf_path}")
        return

    try:
        # 以二进制读取模式打开 PDF
        # 以写入模式打开 TXT，encoding='utf-8' 确保中文不乱码
        with open(pdf_path, 'rb') as pdf_file, open(txt_path, 'w', encoding='utf-8') as out_file:
            # 创建 PdfReader 对象
            reader = PyPDF2.PdfReader(pdf_file)
            
            # 获取 PDF 总页数
            num_pages = len(reader.pages)
            print(f"正在处理文件: {pdf_path} (共 {num_pages} 页)\n")
            print(f"结果将保存至: {txt_path}\n")

            # 遍历每一页
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                
                # 提取当前页的文本
                text = page.extract_text()
                
                # 按行分割文本
                lines = text.split('\n')
                
                # 写入页码标记
                out_file.write(f"--- 第 {page_num + 1} 页 ---\n")
                
                for line in lines:
                    # 写入每一行（去除首尾空白）
                    out_file.write(line.strip() + '\n')
                
                out_file.write("\n") # 页与页之间空一行

        print("处理完成。")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 默认 PDF 文件名
    pdf_file = 'example.pdf'
    
    # 如果命令行有参数，则使用命令行参数
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]
    
    # 自动生成输出文件名：将扩展名 .pdf 替换为 .txt
    base_name = os.path.splitext(pdf_file)[0]
    txt_file = f"{base_name}.txt"
        
    save_pdf_to_txt(pdf_file, txt_file)
