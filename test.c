#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define  S_SIZE 0x2000

unsigned long j_1[S_SIZE];
unsigned long j_2[S_SIZE];
unsigned long j_3[S_SIZE];

#if 0
int init_test(unsigned long *j_1, unsigned long *j_2, unsigned long *j_3){
	int i;

	for(i = 0x0; i<S_SIZE; i++){
		j_1[i] = i;
		j_2[i] = i;
		j_3[i] = i;
	}
}
#endif

int main(int argc, char *argv[]){
	unsigned long i, j;
	char buff[1000];

	sprintf(buff, "pmap -X %d", getpid());
	system(buff);

	sleep(30);

	for(i = 0x0; i<S_SIZE; i++) {
		for(j = 0x0; j < S_SIZE; j++) {
			j_1[j] = i;
			j_2[j] = i;
			j_3[j] = i;
		}
	}
	
	for(i = 0x0; i<S_SIZE; i++) {
		for(j = 0x0; j < S_SIZE; j++) {
			j_1[j] = i;
			j_2[j] = i;
		}
	}
	
	for(i = 0x0; i<S_SIZE; i++) {
		for(j = 0x0; j < S_SIZE; j++) {
			j_1[j] = i;
		}
	}
}
