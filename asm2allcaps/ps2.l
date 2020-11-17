%{ 
 // #include "y.tab.h"

%}

%%
[;].* {fprintf(yyout, "");}

[a-z] {fprintf(yyout,"%c",yytext[0]-32);}

. {fprintf(yyout, "%s", yytext); }
%%

yywrap();

int main()
{

	extern FILE *yyin, *yyout; 
  
    yyin = fopen("asm_code.txt", "r"); 
  
    yyout = fopen("asm_out_code.txt", "w"); 
	yylex();
	return 0;

}

