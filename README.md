# Local_Wikipedia
Deploy Wikipedia locally and mimic the functions of [Search() and Lookup()] 
  Deploy Wikipedia locally:
    Tool:Kiwix
    Step:  
    1、Download the Kiwix toolkit.  
    wget https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-x86_64.tar.gz<br>
    2、Unzip the downloaded file.  
    tar -xzf kiwix-tools_linux-x86_64.tar.gz<br>
    3、Install the ZIM package:
    Select the version that suits you. Here, I choose the nopic version without images. <br>
     a)https://www.mirrorservice.org/sites/download.kiwix.org/zim/wikipedia/<br>
     b)mkdir zims <br>
     c)cd zims<br>
     d)wget https://www.mirrorservice.org/sites/download.kiwix.org/zim/wikipedia/wikipedia_en_all_nopic_2024-06.zim<br>
