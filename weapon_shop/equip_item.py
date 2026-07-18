# =====================================================
#  weapon_shop/equip_item.py — คนรับผิดชอบ: ______________________
#  หน้าที่: ซื้อและสวมใส่อาวุธให้ลูกน้อง (เช็คเงื่อนไข 2 อย่างก่อน)
# =====================================================

def equip_item(person, weapon):
    current_money = person["money"]
    weapon_owned = person["equipment"]
    purchase = False
    while True:
        if weapon_owned == "ไม่มี":
            if current_money < 10000:
                purchase = False
                messenger = f"คุณมีเงินไม่พอซื้ออาวุธ"
                return {"status": False, "message": messenger}
            if current_money >=10000 and current_money < 50000:
                current_money -= 10000
                person["power"] += 2
                power_outcome = person["power"]
                person["money"] = current_money
                money_outcome = person["money"]
                person["equipment"] = "มี"
                messenger = f"คุณมีเงินพอที่จะซื้ออาวุธ สนับมือ\nการซื้อสำเร็จ!\nยอดคงเหลือของคุณ {money_outcome} บาท\nค่าพลังของคุณในตอนนี้ คือ {power_outcome}\nยินดีด้วยตอนนี้คุณได้ครอบครองอาวุธแล้ว"
                return {"status": True, "message": messenger}
            if current_money <= 150000:
                while True:
                    choose_weapon = int((input(f"\nคุณต้องการอาวุธชิ้นไหนจากตัวเลือกต่อไปนี้\n1 สนับมือ\n2 ปืนพก 9mm\nอาวุธที่คุณเลือกคือ: ")))
                    if choose_weapon == 1:
                        current_money -= 10000
                        person["power"] += 2
                        power_outcome = person["power"]
                        person["money"] = current_money
                        money_outcome = person["money"]
                        person["equipment"] = "มี"
                        messenger = f"คุณมีเงินพอที่จะซื้ออาวุธ สนับมือ\nการซื้อสำเร็จ!\nยอดคงเหลือของคุณ {money_outcome} บาท\nค่าพลังของคุณในตอนนี้ คือ {power_outcome}\nยินดีด้วยตอนนี้คุณได้ครอบครองอาวุธแล้ว"
                        return {"status": True, "message": messenger}
                    elif choose_weapon == 2:
                        current_money -= 50000
                        person["power"] += 5
                        power_outcome = person["power"]
                        person["money"] = current_money
                        money_outcome = person["money"]
                        person["equipment"] = "มี"
                        messenger = f"คุณมีเงินพอที่จะซื้ออาวุธ 9mm\nการซื้อสำเร็จ!\nยอดคงเหลือของคุณ {money_outcome} บาท\nค่าพลังของคุณในตอนนี้ คือ {power_outcome}\nยินดีด้วยตอนนี้คุณได้ครอบครองอาวุธแล้ว"
                        return {"status": True, "message": messenger}
                    else:
                        print("กรุณาเลือกตัวเลือกจากรายการก่อนหน้า")
                        print(f"\n-----------")
            if current_money >= 150000:
                while True:
                    choose_weapon = (input(f"\nคุณต้องการอาวุธชิ้นไหนจากตัวเลือกต่อไปนี้\n1 สนับมือ\n2 ปืนพก 9mm\n3 ปืนกล Thompson\nอาวุธที่คุณเลือกคือ: "))
                    if choose_weapon == 1:
                        current_money -= 10000
                        person["power"] += 2
                        power_outcome = person["power"]
                        person["money"] = current_money
                        money_outcome = person["money"]
                        person["equipment"] = "มี"
                        messenger = f"คุณมีเงินพอที่จะซื้ออาวุธ สนับมือ\nการซื้อสำเร็จ!\nยอดคงเหลือของคุณ {money_outcome} บาท\nค่าพลังของคุณในตอนนี้ คือ {power_outcome}\nยินดีด้วยตอนนี้คุณได้ครอบครองอาวุธแล้ว"
                        return {"status": True, "message": messenger}
                    elif choose_weapon == 2:
                        current_money -= 50000
                        person["power"] += 5
                        power_outcome = person["power"]
                        person["money"] = current_money
                        money_outcome = person["money"]
                        person["equipment"] = "มี"
                        messenger = f"คุณมีเงินพอที่จะซื้ออาวุธ 9mm\nการซื้อสำเร็จ!\nยอดคงเหลือของคุณ {money_outcome} บาท\nค่าพลังของคุณในตอนนี้ คือ {power_outcome}\nยินดีด้วยตอนนี้คุณได้ครอบครองอาวุธแล้ว"
                        return {"status": True, "message": messenger}
                    elif choose_weapon == 3:
                        current_money -= 150000
                        person["power"] += 10
                        power_outcome = person["power"]
                        person["money"] = current_money
                        money_outcome = person["money"]
                        person["equipment"] = "มี"
                        messenger = f"คุณมีเงินพอที่จะซื้ออาวุธ ปืนกล Thompson\nการซื้อสำเร็จ!\nยอดคงเหลือของคุณ {money_outcome} บาท\nค่าพลังของคุณในตอนนี้ คือ {power_outcome}\nยินดีด้วยตอนนี้คุณได้ครอบครองอาวุธแล้ว"
                        return {"status": True, "message": messenger}
                    else:
                        print("กรุณาเลือกตัวเลือกจากรายการก่อนหน้า!")
                        print(f"\n-----------")
        elif weapon_owned == "มี":
            return {"status": False, "message": messenger}
        else:
            print("กรุณาเลือกตัวเลือกจากรายการก่อนหน้า!")
            print(f"\n-----------")
        




#   - เช็คเงิน: เงินของ person ไม่พอราคา weapon -> ซื้อไม่ได้
#   - เช็คอาวุธ: person มีอาวุธอยู่แล้ว (equipment ไม่ใช่ "ไม่มี") -> ใส่เพิ่มไม่ได้
#   - ผ่านทั้งคู่ -> หักเงิน, เปลี่ยน equipment เป็นชื่ออาวุธ, บวก bonus เข้า power
#   - return {"status": True/False, "message": ข้อความบอกผล}
    # TODO: เขียนโค้ดตรงนี้
    pass


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.equip_item
if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}

    print(equip_item(vito, gun))   # ต้องได้ status True
    print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    print(equip_item(vito, gun))   # ครั้งที่สองต้องได้ "มีอาวุธอยู่แล้ว"
