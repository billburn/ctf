# Terminal Challenges

## CURLing Master (HHC 2018)
[URL] https://docker.kringlecon.com/?challenge=http2&id=51d42434-81cd-4850-a5a7-02d8f3edee30
```
1) Figure out how to curl using http2 (--http2-prior-knowledge)
2) Figure out how to send a post request (-X POST)
3) Figure out how to send parameter (-d "status=on")
curl -X POST -d "status=on" --http2-prior-knowledge http://localhost:8080
```
![Curling Master](https://github.com/billburn/ctf/blob/master/H2%20Matrix/Images/curlingmaster-01.png)

## The Name Game Terminal Challenge
[URL] https://docker.kringlecon.com/?challenge=pwshmenu&id=fb959815-faef-43e8-b792-67398d577b5b
```
1) Run the program to see what options we have
2) I tried command injection and it worked (127.0.0.1; pwd)
3) I used this command injection to enumerate the files and cat the database (127.0.0.1; ls -lah)
3a) (127.0.0.1; cat onboard.db) to get Mr. Chan's first name
4) Finally, ran the runtoanswer binary (127.0.0.1; ./runtoanswer)
```
![Name Game](https://github.com/billburn/ctf/blob/master/H2%20Matrix/Images/namegame-01.png)

## The Sleighbell Terminal Chllenge
[URL] https://docker.kringlecon.com/?challenge=unlinked-function&id=cac82b3d-199a-4ba1-b4e7-ffa566a0c370
```
1) Run the program and see what happens
2) Run the program in GDB and list the functions (gdb -q sleighbell-lotto)
2a) (gdb) info functions
2b) We have a few functions that might be interesting (base64_decode and winnerwinner)
3) Using the writeup from Ron Bowes: [GDB] https://www.sans.org/blog/using-gdb-to-call-random-functions/ we might try simply jumping to the function
4) First set a break at main (break main)
5) Once the breakpoint is hit, let's jump to "winnerwinner" and continue execution
6) Voila!  That will do it
```
![Sleighbell Lotto](https://github.com/billburn/ctf/blob/master/H2%20Matrix/Images/sleighbell-lotto-01.png)

## Lethal ForensicELFication Terminal Challenge
[URL] https://docker.kringlecon.com/?challenge=viminfo&id=e2632477-e60f-497b-8c9b-d4b4cdd07a68
```
1) Run the program and see what happens
2) Check the directory structure to see what files are there (ls -lah)
3) Run cat on the .bash_history and .viminfo files (cat .bash_history && cat .viminfo)
4) We have a name "Elinore" at the top that looks to be a substitution, which the .bash_history suggests
5) Run runtoanswer and that will do it (./runtoanswer)
```
![Lethal ForensicELFication](https://github.com/billburn/ctf/blob/master/H2%20Matrix/Images/viminfo-01.png)