#!/bin/bash

# 配置
hostname="您在Cloudflare上的域名"
email=“您在Cloudflare註冊的郵箱”

zone_id=“您在Cloudflare上的域名區域 ID”
global_api_key=“您在Cloudflare上的API 密鑰”



# =============以下不需要修改====================
ipAddr="`curl https://ifconfig.co`"
url="https://api.cloudflare.com/client/v4/..."

# 獲取cloudflare記錄ID
listDnsApi="${url}/${zone_id}/dns_records?type=A&name=${hostname}"
res=$(curl -s -X GET "$listDnsApi" -H "X-Auth-Email:$email" -H "X-Auth-Key:$global_api_key" -H "Content-Type:application/json")
recordId=$(echo "$res" | jq -r ".result[0].id")

# 更新cloudflare記錄
updateDnsApi="${url}/${zone_id}/dns_records/${recordId}";
data="{\"type\":\"A\",\"name\":\"${hostname}\",\"content\":\"${ipAddr}\",\"ttl\":60,\"proxied\":false}"
res=$(curl -s -X PUT "$updateDnsApi" -H "X-Auth-Email:$email" -H "X-Auth-Key:$global_api_key" -H "Content-Type:application/json" --data "$data")

# 打印結果
echo "$res"