
import os
import xml.etree.ElementTree as ET

ET.register_namespace('','http://maven.apache.org/POM/4.0.0')
#获取xml文件地址
path = os.path.abspath('.')
data_path = os.path.join(path,'pom.xml') #获取xml文件地址
tree = ET.parse(data_path)
root = tree.getroot()

namespaces = '{http://maven.apache.org/POM/4.0.0}'


def get_data_vaule(style, type_name, change_value):
    target = root.find(namespaces+style)
    sdk_v = target.find(namespaces+type_name)
    if (sdk_v is not None):
        sdk_v.text = change_value
        print(sdk_v.text)
    return


text = get_data_vaule('properties','Sdk.version','2.2.2')
tree.write("new_dimen.xml", xml_declaration=True, encoding="UTF-8")