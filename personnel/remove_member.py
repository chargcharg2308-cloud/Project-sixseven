# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: โฟม
#  หน้าที่: ลบลูกน้องออกจากแฟมิลี่ตามชื่อ
# =====================================================
from data import family_members

def remove_member(target_name):
#   - หาคนที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก) แล้วลบออกจาก family_members
#   - ลบสำเร็จ -> return True | ไม่เจอ -> return False
    # TODO: เขียนโค้ดตรงนี้
    family_members = input("Enter remove name : ")
    for person_dict in family_members:
        if person_dict["name"] == target_name:
            family_members.remove(person_dict)
            if True:
                print("สั่งเก็บเรียบร้อย")        
    return "ไม่พบชื่อในระบบ"


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.remove_member
if __name__ == "__main__":
    print(remove_member("Luigi"))   # ครั้งแรกต้องได้ True
    print(remove_member("Luigi"))   # ครั้งที่สองต้องได้ False (ลบไปแล้ว)
    print(family_members)           # ต้องเหลือแค่ Tony
