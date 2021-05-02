grammar BKIT;
//MSSV: 1814315
@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}
/*
*
*       PARSER
*
 */
program
    : manydeclaration? EOF
    ;
manydeclaration
    : declarations manydeclaration
    | declarations
    ;
declarations
    : var_declarations
    | main_statement
    ;

/*--Variable Declaration--*/
var_declarations
    : VAR COLON variable_list SEMI
    ;
variable_list
    : var_part COMMA variable_list
    | var_part
    ;
var_part
    : init_var
    | un_init_var
    ;
un_init_var
    : ID
    | ID dimension
    ;
init_var
    : ID SINGLE_EQUAL normal_literals
    | ID dimension SINGLE_EQUAL array_literal
    ;
var_name
    : ID
    | ID dimension
    ;
dimension
    : LSB INTLIT RSB dimension
    | LSB INTLIT RSB
    ;
normal_literals
    : INTLIT
    | FLOATLIT
    | TRUE
    | FALSE
    | STRING
    | one_array
    ;
/*---Statement---*/
main_statement
    : FUNCTION COLON ID (PARAMETER COLON parameter_list)? BODY COLON var_body? statement_lists? ENDBODY DOT
    ;
parameter_list
    : un_init_var COMMA parameter_list
    | un_init_var
    ;
var_body
    : var_declarations var_body
    | var_declarations
    ;
//Assignment statement
statement_lists
    : statement_list statement_lists
    | statement_list
    ;
statement_list
    : assign_statement
    | if_statement
    | for_statement
    | while_statement
    | do_while_statement
    | break_statement
    | continue_statement
    | call_statement
    | return_statement
    | var_declarations
    ;
assign_statement
    : lhs SINGLE_EQUAL exp SEMI
    ;
lhs
    : ID
    | index_expression
    ;
body_part
    : var_body? statement_lists?
    ;
//If statement
if_statement
    : IF exp THEN var_body? statement_lists? elseif_part? else_part? ENDIF DOT
    ;
elseif_part
    : ELSEIF exp THEN var_body? statement_lists? elseif_part
    | ELSEIF exp THEN var_body? statement_lists?
    ;
else_part
    : ELSE var_body? statement_lists?
    ;
//For statement
for_statement
    : FOR LRB ID SINGLE_EQUAL init_exp COMMA condition_exp COMMA update_exp RRB DO var_body? statement_lists? ENDFOR DOT
    ;
init_exp
    : exp
    ;
condition_exp
    : exp
    ;
update_exp
    : exp
    ;
//While statement
while_statement
    : WHILE exp DO body_part ENDWHILE DOT
    ;
//Do-while statement
do_while_statement
    : DO body_part WHILE exp ENDDO DOT
    ;
//Break statement
break_statement
    : BREAK SEMI
    ;
//Continue statement
continue_statement
    : CONTINUE SEMI
    ;
//Call statement
call_statement
    : function_call SEMI
    ;
//Return statement: must in function
return_statement
    : RETURN exp? SEMI
    ;
/*---Expression---*/
exp
    : exp1 EQUAL             exp1
    | exp1 NOTEQUALINT       exp1
    | exp1 LESSTHANINT       exp1
    | exp1 GREATERTHANINT    exp1
    | exp1 LESSEQUALINT      exp1
    | exp1 GREATEREQUALINT   exp1
    | exp1 NOTEQUALFLOAT     exp1
    | exp1 LESSTHANFLOAT     exp1
    | exp1 GREATERTHANFLOAT  exp1
    | exp1 LESSEQUALFLOAT    exp1
    | exp1 GREATEREQUALFLOAT exp1
    | exp1
    ;
//lhs_exp
//    : exp1
//    ;

exp1    //&&,||
    : exp1 AND              exp2
    | exp1 OR               exp2
    | exp2
    ;
exp2    //+.+.,-,-.
    : exp2 ADDINT           exp3
    | exp2 ADDFLOAT         exp3
    | exp2 SUBINT           exp3
    | exp2 SUBFLOAT         exp3
    | exp3
    ;
exp3    // *,*.,\,\.,%
    : exp3 MULINT           exp4
    | exp3 MULFLOAT         exp4
    | exp3 DIVINT           exp4
    | exp3 DIVFLOAT         exp4
    | exp3 MOD              exp4
    | exp4
    ;
exp4    //!
    : NOT                   exp4
    | exp5
    ;
exp5    //-,-.
    : SUBFLOAT              exp5
    | SUBINT                exp5
    | exp6
    ;
exp6    //index [,]
    : literals
    | LRB exp RRB
    | index_expression
    | function_call
//    | LSB exp RSB
    ;
literals
    : ID
    | INTLIT
    | FLOATLIT
    | TRUE
    | FALSE
    | STRING
    | array_name
    | array_literal
    ;
array_name
    : ID dimen
    ;
dimen
    : LSB exp RSB dimen
    | LSB exp RSB
    ;
index_expression
    : index_expression_name index_operator
    ;
index_operator
    : LSB exp RSB
    | LSB exp RSB index_operator
    ;
index_expression_name
    : ID
    | function_call
    ;
function_call
    : ID LRB argument_list? RRB
    ;
argument_list
    //: (exp (COMMA exp)*)?
    : exp COMMA argument_list
    | exp
    ;
array_literal
    : LB (array_value | one_array | many_array) RB
    ;
many_array
    : one_array many_array
    | one_array
    ;
one_array
    : LB array_value RB
    ;
array_value
//    : normal_literals COMMA array_value
    : normal_literals (COMMA normal_literals)*
    ;
/*
*
*        LEXER
*
*/
//Characters Set
WS : [ \t\f\r\n]+ -> skip ;

//Comment
COMMENT: '**' .*? '**' -> skip;

//Token Set
//Identifiers
ID
    :[a-z] [_a-zA-Z0-9]*
    ;

//This for KeyWords
BODY:       'Body';
ELSE:       'Else';
ENDFOR:     'EndFor';
IF:         'If';
VAR:        'Var';
ENDDO:      'EndDo';
BREAK:      'Break';
ELSEIF:     'ElseIf';
ENDWHILE:   'EndWhile';
PARAMETER:  'Parameter';
WHILE:      'While';
CONTINUE:   'Continue';
ENDBODY:    'EndBody';
FOR:        'For';
RETURN:     'Return';
TRUE:       'True';
DO:         'Do';
ENDIF:      'EndIf';
FUNCTION:   'Function';
THEN:       'Then';
FALSE:      'False';

//This for Operators
ADDINT:             '+';
ADDFLOAT:           '+.';
SUBINT:             '-';
SUBFLOAT:           '-.';
MULINT:             '*';
MULFLOAT:           '*.';
DIVINT:             '\\';
DIVFLOAT:           '\\.';
MOD:                '%';
NOT:                '!';
AND:                '&&';
OR:                 '||';
SINGLE_EQUAL:       '=';
EQUAL:              '==';
NOTEQUALINT:        '!=';
LESSTHANINT:        '<';
GREATERTHANINT:     '>';
LESSEQUALINT:       '<=';
GREATEREQUALINT:    '>=';
NOTEQUALFLOAT:      '=/=';
LESSTHANFLOAT:      '<.';
GREATERTHANFLOAT:   '>.';
LESSEQUALFLOAT:     '<=.';
GREATEREQUALFLOAT:  '>=.';

//This for Separators
LRB:    '(';//Round bracket
RRB:    ')';
LSB:    '[';//Square bracket
RSB:    ']';
LB:     '{';//Bracket
RB:     '}';
COLON:  ':';
DOT:    '.';
COMMA:  ',';
SEMI:   ';';
UNDERSCORE: '_';

//This for literals
//Integer
fragment DEC
    : [0-9]
    | [1-9][0-9]*
    ;
fragment HEX: '0' [xX] [0-9A-F]*;
fragment OCT: '0' [oO] [0-7]*;
INTLIT
    : DEC
    | HEX
    | OCT
    ;

//Float
fragment EXP: [eE] [+-]? [0-9]+;
fragment Decimal: '.' [0-9]*;
FLOATLIT
    : DEC Decimal? EXP
    | DEC Decimal EXP?
    ;

//Boolean
BOOLEAN: TRUE | FALSE;

//String
STRING
    : '"' ('\\\\'|'\\t'|'\\\''|'\\n'|'\\f'|'\\r'|'\\b'|'\'"'| ~[\n\r'"\\] )* '"'
    {
        self.text=self.text[1:-1]
    }
    ;

//Array
//fragment ARRAY_ELEMENT
//    : INTLIT | FLOATLIT | BOOLEAN | STRING
//    ;
//fragment SUB_ARRAY
//    : '{' SPACE* SUB_ARRAY SPACE* (',' SPACE* SUB_ARRAY )* SPACE* '}'
//    | ARRAY_ELEMENT
//    ;
//
//fragment SPACE
//    : ' '
//    ;
//ARRAY
//    // : '{'ARRAY_ELEMENT (',' ARRAY_ELEMENT)* '}'
//    // | '{' (SPACE*)? '{'ARRAY_ELEMENT (',' ARRAY_ELEMENT)* '}' (',' '{'ARRAY_ELEMENT (',' ARRAY_ELEMENT)* '}')* (SPACE*)?'}'
//    : '{' SPACE* SUB_ARRAY SPACE* (',' SPACE* SUB_ARRAY SPACE* )*'}'
//    {
//        self.text = self.text.replace(" ", "")
//        self.text = self.text.replace("\n", "")
//    }
//    ;

ILLEGAL_ESCAPE
 	: '"' ('\\\\'|'\\t'|'\\\''|'\\n'|'\\f'|'\\r'|'\\b'|'\'"'| ~[\n\r\b\f\t'"\\] )* '\\' (~[bfrnt'"\\] (~'"')*)? '"'
	{
		for x in range(len(self.text)):
			if self.text[x] == '\\':
	  			if (self.text[x+1] == 'b') or (self.text[x+1] == 'f') or (self.text[x+1] == 'r') or (self.text[x+1] == '"n"'):
				    continue
	  			elif (self.text[x+1] == 'n') or (self.text[x+1] == 't') or (self.text[x+1] == '\'') or (self.text[x+1] == '\\'):
				    continue
	  			elif (x+1)==(len(self.text)) :
				    x=x-1
				    break
	  			else:
				    break
			elif self.text[x] == "\'":
	  			x=x-1
	  			break
		raise IllegalEscape(self.text[1:x+2])
	}
   	;
UNCLOSE_STRING
 	: '"' ('\\\\'|'\\t'|'\\\''|'\\n'|'\\f'|'\\r'|'\\b'|'\'"'| ~[\n\r'"\\] )* [\n\r]?
	{
		raise UncloseString(self.text[1:])
	}
   	;



ERROR_CHAR
 	: .
	{
		raise ErrorToken(self.text[0:])
	}
   	;
UNTERMINATED_COMMENT
    : '**' .*? '*'
    | '**' .*?
    {
        raise UnterminatedComment()
    }
    ;
