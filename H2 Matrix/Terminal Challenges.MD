# Terminal Challenges

## CURLing Master (HHC 2018)
[URL] https://docker.kringlecon.com/?challenge=http2&id=51d42434-81cd-4850-a5a7-02d8f3edee30
```
1) Figure out how to curl using http2 (--http2-prior-knowledge)
2) Figure out how to send a post request (-X POST)
3) Figure out how to send parameter (-d "status=on")
curl -X POST -d "status=on" --http2-prior-knowledge http://localhost:8080
```

## The Name Game Terminal Challenge
[URL] https://docker.kringlecon.com/?challenge=pwshmenu&id=fb959815-faef-43e8-b792-67398d577b5b
```
1) Run the program to see what options we have
2) I tried command injection and it worked (127.0.0.1; pwd)
3) I used this command injection to enumerate the files and cat the database (127.0.0.1; ls -lah)
3a) (127.0.0.1; cat onboard.db) to get Mr. Chan's first name
4) Finally, ran the runtoanswer binary (127.0.0.1; ./runtoanswer)
```
![TEST] (https://github.com/billburn/ctf/blob/master/H2%20Matrix/Images/namegame-01.png "Some text")