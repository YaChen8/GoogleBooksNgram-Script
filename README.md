# GoogleBooksNgram-Script

下载Google Books Ngram Viewer数据
https://books.google.com/ngrams/

## 简单用法示例

下载所有代码后在setup.py文件夹位置按住Shift键同时鼠标右击，点击“在此处打开Powershell窗口”

![image-1658900850938](http://www.chenya.online/upload/2022/07/image-1658900850938.png)

打开代码行界面后输入下方的代码然后按回车，运行完对应的代码行后会在data的文件夹位置输出保存的结果

    python .\getNgrams.py virus,toxin,vira,virion,venom -corpus=eng_2019 -startYear=1500 -endYear=2019 -smoothing=3 -csv -quit  -noprint

Flags:

    -corpus=检索使用的语料库，大概有eng_2012, eng_2009, eng_us_2012, eng_us_2009, eng_gb_2012, eng_gb_2009, chi_sim_2012, chi_sim_2009, fre_2012, fre_2009, ger_2012, ger_2009,spa_2012, spa_2009, rus_2012, rus_2009, heb_2012, heb_2009, ita_2012,	eng_fiction_2012, eng_fiction_2009, eng_1m_2009 [默认: eng_2019]
    详细内容可以去该网页查找http://books.google.com/ngrams/info.
    
    -startYear=查询开始年份 [默认: 1500]
    
    -endYear=查询截至年份 [默认: 2019]
    
    -smoothing=曲线平滑系数 [默认: 3]
    
    -nosave 该参数表示不保存
    
    -csv 该参数表示保存为csv表格
    
    -noprint 该参数表示为结果不在运行界面输出
    
    -help
    
    -quit 添加这个参数后运行完代码直接退出

## 批量下载示例

将需要下载的关键词按行存储在subjects.txt文件里面


然后运行get_all subjects.py文件，最终数据会依次存储在data文件夹里，如果需要修改下载的flags，可以直接打开get_all subjects.py文件修改command对应的参数

