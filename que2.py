question = ["Python","java","Odoo","magento","Asp","Aps1"]
vowels = ["A","E","I","O","U"]

output = [ele for ele in question if ele.isalpha and ele[0].isupper() and ele[0] not in vowels]
print(output)