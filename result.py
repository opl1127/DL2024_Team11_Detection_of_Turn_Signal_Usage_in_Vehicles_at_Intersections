def analyze_detection_results(file_path):
    
    r_s = False
    l_s = False
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            r_count = line.count("右轉")
            if "右轉" in line and "有打方向燈" in line and r_count == 2:
                r_s = True
        for line in lines:
            l_count = line.count("左轉")
            if "左轉" in line and "有打方向燈" in line and l_count == 2:
                l_s = True
                    
    print(r_s)
    print(l_s)               
    if (r_s==True and l_s ==False):
        print("右轉車輛正確施打方向燈")
    elif (r_s==False and l_s ==True):
        print("左轉車輛正確施打方向燈")
    elif (r_s==True and l_s ==True):
        print("右轉與左轉車輛皆正確施打方向燈")        
    else:
        print("車輛未正確施打方向燈")

# 假設結果保存在 results.txt 文件中
analyze_detection_results('/home/opl/Desktop/DL_out/output.txt')

