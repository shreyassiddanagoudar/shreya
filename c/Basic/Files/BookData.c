#include <stdio.h>
#include <string.h>

#define MAX_BOOK_NUM 1000
struct book {
    char title[128];
    char author[128];
    int prize;
    int  numcopies ; 
    int  year ;
    int uniqueid;
    int stock;
} ;

struct book bks[MAX_BOOK_NUM] ;
    
void add() {
    int index=0;
    printf("\n title1:");
    scanf("%s", bks[0].title);
    printf("\n author");
    scanf("%s", bks[index].author);
    // strcpy(bks[0].author);
    printf("\n prize:");
    scanf("%d", &bks[index].prize);
    printf("\n numcopies:");
    scanf("%d", &bks[index].numcopies);
    printf("\n year:");
    scanf("%d", &bks[index].year);
    printf("\n uniqueid");
    scanf("%d", &bks[index].uniqueid);
    printf("Added %s %s %d %d %d %d \n", bks[0].title, bks[index].author, bks[index].prize,  bks[index].numcopies, bks[index].year, bks[index].uniqueid);

}

void write() {
    FILE *fp = fopen("books1.data","w") ;
    if (fp != NULL) {
        fwrite(&bks, sizeof(struct book), 1, fp) ; 
        printf("Saved to file!!!\n");
    }
    fclose(fp);
    return ;
}

void read() {
    FILE *fp = fopen("books1.data","r") ;
    struct book bk[3];
    if (fp != NULL) {
        fread(&bk, sizeof(struct book), 1, fp) ; 
    }
    fclose(fp);
    printf("%s\n", bk[0].title);
    printf("%s\n", bks[0].author);
    printf("%d\n", bks[0].prize);
    printf("%d\n", bks[0].numcopies);
    printf("%d\n", bk[0].year);
    printf("%d\n", bks[0].uniqueid);
    return ;
}

int main() {
    char choice;
    printf("Welcome to binary system\n");
    printf("available options\n");
    printf("a-add the books\n m-modify the book number\n d-delet the number\n v-view\n s-save the library data type\n l-list all the book details\n q-quit\n h-help\n");
    scanf("%c",&choice);
    switch(choice) {
        case'a':add();
        break;
        /*case 'm':modify();
        break;
        case 'd':delete();
        break;
         case'v':view();
        break;
        case 's':save();
        break;
        case 'l':list();
        break;
        case 'q':quit();
        break;
        case 'h':help();
        break;*/
        
    }
    //  init();
     write();
    read();
    return 0;
}