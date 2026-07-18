# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
#  หน้าที่: แสดงรายชื่อลูกน้องทั้งหมดในแฟมิลี่
# =====================================================
from data import family_members

def show_members():
    for family_member in family_members:
#   - print ข้อมูลลูกน้องทุกคนใน family_members บรรทัดละคน (ชื่อ, ตำแหน่ง, ความโหด, อาวุธ) 
        name = family_member['name']
        age = family_member['age']
        role = family_member['role']
        power = family_member['power'] 
        money = family_member['money'] 
        equipment = family_member['equipment'] 
        print (f"{name}, {age},{role},{power},{money},{equipment}")
# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python  python -m personnel.show_members
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด

