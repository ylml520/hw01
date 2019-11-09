import re

def check_id_card(id_card):

    errors = ['验证通过!', '身份证号码位数不对!',  '身份证号码出生日期超出范围或含有非法字符!', '身份证号码校验错误!', '身份证地区非法!']

    area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江",

            "31": "上海", "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北",

            "43": "湖南", "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏",

            "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门"} 

    id_card = str(id_card)

    id_card = id_card.strip()

    id_card_list = list(id_card)

 

    if len(id_card) == 18:

        if not area[id_card[0:2]]:

            print(errors[4])
        
        if int(id_card[6:10])< 1900 and int(id_card[6:10])> 2019:
            
            print(errors[2]) 
 
        if int(id_card[6:10]) % 4 == 0 or (int(id_card[6:10]) % 100 == 0 and int(id_card[6:10]) % 4 == 0):

            e_reg = re.compile(

                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'

                '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
            
        else:

            e_reg = re.compile(

                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'

                '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')
            
        if re.match(e_reg, id_card):


            S = (int(id_card_list[0]) + int(id_card_list[10])) * 7 + (
                        
                        int(id_card_list[1]) +int(id_card_list[11])) * 9 + (
                        
                        int(id_card_list[2]) + int(id_card_list[12])) * 10 + (
                        
                        int(id_card_list[3]) + int(id_card_list[13])) * 5 + (
                        
                        int(id_card_list[4]) + int(id_card_list[14])) * 8 + (

                        int(id_card_list[5]) + int(id_card_list[15])) * 4 + (

                        int(id_card_list[6]) + int(id_card_list[16])) * 2 + (
                
                        int(id_card_list[7])) * 1 + (
                        
                        int(id_card_list[8])) * 6 + (
                        
                        int(id_card_list[9]))* 3

            Y = S % 11
            
            M = "F"

            JYM = "10X98765432"

            M = JYM[Y]

            if M == id_card_list[17]:

                print(errors[0])
                
                place=id_card[0:2]

                birthplace=area[place]

                print("地址："+birthplace+'省/直辖市')
        
                year=id_card[6:10]
            
                moon=id_card[10:12]
            
                day=id_card[12:14]
            
                print("生日: "+year+'年'+moon+'月'+day+'日')
                
                if int(id_card[14:17])%2==0:
                
                    print('性别：女')
                
                else:
                    
                    print('性别：男')

            else:

                print(errors[3])

        else:

            print(errors[2])

    else:

        print(errors[1])



if __name__ == "__main__":

    while True:

        input_card = input("请输入你的身份证号：")

        if input_card == "exit":

            print("程序已结束！")

            break

        else:

            check_id_card(input_card)
