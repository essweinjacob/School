#include <stdio.h>
#include <unistd.h>

void main(){
    int pid;

    printf("OG Process with PID %d and PPID %d. \n",getpid(), getppid());
    pid = fork();

    if(pid !=0){
        printf("Success\n");
        printf("parent pid %d and ppid %d\n", getpid(), getppid());
        printf("Child pid is %d\n", pid);
    }
    else {
        sleep(5);

        printf("Failure\n");
        printf("child process with pid %d and ppid %d\n", getpid(), getppid());
    }
    printf("PID %d terminates\n", getpid());
}
