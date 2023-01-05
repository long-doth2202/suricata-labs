# DÒ QUÉT VÀ TẤN CÔNG MẠNG

## Môn Quản trị mạng - 3//, PGS. TS Tạ Minh Thanh

## Các thành viên đóng góp

- Đỗ Thành Long
- Vũ Thái An

## Chức năng

- Dò quét các cổng được mở trên thiết bị kết nối chung mạng
- Lợi dụng quá trình bắt tay ba bước để tiến hành SYN flood attack

## Suricata rules

restart -> apply enss33

alert ICMP any any -> $HOME_NET any (msg: "Ping detection"; sid:1000000; rev:1;)
drop ICMP any any -> $HOME_NET any (msg:"ET DROP ping from any"; sid: 3000005; rev:1;)
drop tcp any any -> $HOME_NET any (msg:"ET DROP TCP from any"; sid: 3000006; rev:1;)
