def format_text(text, max_line_length):
    formatted_text = []
    paragraphs = text.split('\n\n') 
    
    for paragraph in paragraphs:
        lines = paragraph.split('\n') 
        
        for line in lines:
            words = line.split() 
            formatted_line = '    '  
            
            for word in words:
                if len(formatted_line) + len(word) <= max_line_length:  
                    if formatted_line != '    ':  
                        formatted_line += ' '
                    formatted_line += word
                else:
                    formatted_text.append(formatted_line) 
                    formatted_line = '    ' + word
            formatted_text.append(formatted_line)
            
        formatted_text.append('')
    
    return formatted_text

def main():
    with open("Text.txt", "r", encoding="utf-8") as file:
        text = file.read()
    
    max_line_length = int(input("Введите максимальную длину строки: "))
    
    formatted_text = format_text(text, max_line_length)
    formatted_text = [line.strip() for line in formatted_text if line.strip()]
    
    print("\n".join(formatted_text))

if __name__ == "__main__":
    main()
