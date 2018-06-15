{
    'name': 'invku',
    'description':"""

版本说明:
-------------
    - V1.0：实现装配关系的输入和查询,报表的打印
    - V2.0：实现图纸的查看和图纸清单输出
    - V3.0：从零开始，从MS平台移植过来的BOM结构和算法，从而实现输入，输出和呈现BOM表
    - V5.0：系统为研发，技术，采购，销售，库房，质量，财务七大部门的核心业务提供支撑
    """,

    'author':'付东海',
    'summary':'在查询系统起步的信息系统',
    'version':'5.0',
    'website':'www.ythlj.com.cn',
#    'license':'LGPL Version 3',
    'depends':['base','product','sale','account','purchase'],
    'application':True,
    'installable': True,
    'auto_install': False,
    'data': [
        #'security/m_erp_access_rules.xml',
        'views/m_view.xml',
        'views/m_menu.xml',
        'security/ir.model.access.csv',
    ],
    #demo里的数据必须在安装模块时(升级没作用)才会载入，使用noupdate控制载入一次否
    'demo': [
       # 'data/m.part.xml',  
    ],
}
