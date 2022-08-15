<?php
error_reporting(0);
session_start();
/////Key Tool/////
system('clear');
while (true){
$checkkey  = file('xxxxx'); //// Linh Key
echo "\033[1;96mLưu Ý Mỗi Ngày Sẽ Đổi Một Key\n";
echo "\033[1;93mLink lấy key:\033[1;91m xxxxx\n"; /// Link Key Đã tạo ở link1s.com
echo "\033[1;92mNhập Key Để Vào Tool: \033[1;33m";
      $makey = trim(fgets(STDIN));
    if ($makey == $checkkey[0])  {
    sleep(1);
        echo "\033[1;35mKey Dúng Đợi Vào Tool\n";
        break;
    } else {
        echo "\033[1;91mKey Sai Vui Lòng Lấy Lại\n";
        echo "\033[1;93m-------------------------------------------------------------\n";
        sleep(1);
       continue;
       }
}