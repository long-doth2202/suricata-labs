# Thiết lập hệ thống IPS/IDS sử dụng Suricata

## Giới thiệu

- Xây dựng hệ thống IPS/IDS bằng Suricata trên Ubuntu
- Sử dụng python script để tấn công SSH brute-force
- Sử dụng python script để tấn công SYN-flood

## Cài đặt Suricata và thiết lập rules

### Cài đặt Suricata

- Cài đặt từ apt:

  > sudo apt-get install software-properties-common
  > sudo add-apt-repository ppa:oisf/suricata-stable
  > sudo apt-get update
  > sudo apt-get install suricata

- Rules để chặn SYN-flood attack và SSH brute-force:
  > drop ICMP any any -> $HOME_NET any (msg:"ET DROP ping from any"; sid: 3000005; rev:1;)
  > drop ssh $EXTERNAL_NET any -> $HOME_NET 22 (msg:"SERIALIZINGME SCAN Paramiko Based SSH Connections Not Allowed"; flow:established,to_server; content:"SSH-"; content:"paramiko"; within:20; reference:url,www.serializing.me/2015/08/12/ssh-brute-force-and-suricata/; classtype:attempted-admin; sid:3000006; rev:1;)
