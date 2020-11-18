%{ 
 #include<stdio.h>

%}

%%
[;].* {fprintf(yyout, "");}

[a-z] {fprintf(yyout,"%c",yytext[0]-32);}

. {fprintf(yyout, "%s", yytext); }
%%

yywrap();

int main(int argc, char **argv)
{

	extern FILE *yyin, *yyout; 
  	yyin = fopen(argv[1], "r"); 
  	yyout = fopen(argv[2], "w"); 
	yylex();
	return 0;

}

