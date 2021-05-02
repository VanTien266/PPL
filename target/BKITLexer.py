# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u023c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\6\2\u0095\n")
        buf.write("\2\r\2\16\2\u0096\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009f\n")
        buf.write("\3\f\3\16\3\u00a2\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4")
        buf.write("\u00ab\n\4\f\4\16\4\u00ae\13\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3=\7=\u018d\n=\f=\16=\u0190\13=\5=\u0192\n=\3>\3>")
        buf.write("\3>\7>\u0197\n>\f>\16>\u019a\13>\3?\3?\3?\7?\u019f\n?")
        buf.write("\f?\16?\u01a2\13?\3@\3@\3@\5@\u01a7\n@\3A\3A\5A\u01ab")
        buf.write("\nA\3A\6A\u01ae\nA\rA\16A\u01af\3B\3B\7B\u01b4\nB\fB\16")
        buf.write("B\u01b7\13B\3C\3C\5C\u01bb\nC\3C\3C\3C\3C\3C\5C\u01c2")
        buf.write("\nC\5C\u01c4\nC\3D\3D\5D\u01c8\nD\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\7E\u01dc\nE\fE\16E")
        buf.write("\u01df\13E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\3F\3F\7F\u01f6\nF\fF\16F\u01f9\13F\3F\3")
        buf.write("F\3F\7F\u01fe\nF\fF\16F\u0201\13F\5F\u0203\nF\3F\3F\3")
        buf.write("F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\7G\u021a\nG\fG\16G\u021d\13G\3G\5G\u0220\nG\3G\3G\3")
        buf.write("H\3H\3H\3I\3I\3I\3I\7I\u022b\nI\fI\16I\u022e\13I\3I\3")
        buf.write("I\3I\3I\3I\7I\u0235\nI\fI\16I\u0238\13I\3I\5I\u023b\n")
        buf.write("I\5\u00a0\u022c\u0236\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177>\u0081\2\u0083")
        buf.write("\2\u0085?\u0087@\u0089A\u008bB\u008dC\u008fD\u0091E\3")
        buf.write("\2\22\5\2\13\f\16\17\"\"\3\2c|\6\2\62;C\\aac|\3\2\62;")
        buf.write("\3\2\63;\4\2ZZzz\4\2\62;CH\4\2QQqq\3\2\629\4\2GGgg\4\2")
        buf.write("--//\7\2\f\f\17\17$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^")
        buf.write("^ddhhppttvv\3\2$$\4\2\f\f\17\17\2\u0267\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0094\3\2\2")
        buf.write("\2\5\u009a\3\2\2\2\7\u00a8\3\2\2\2\t\u00af\3\2\2\2\13")
        buf.write("\u00b4\3\2\2\2\r\u00b9\3\2\2\2\17\u00c0\3\2\2\2\21\u00c3")
        buf.write("\3\2\2\2\23\u00c7\3\2\2\2\25\u00cd\3\2\2\2\27\u00d3\3")
        buf.write("\2\2\2\31\u00da\3\2\2\2\33\u00e3\3\2\2\2\35\u00ed\3\2")
        buf.write("\2\2\37\u00f3\3\2\2\2!\u00fc\3\2\2\2#\u0104\3\2\2\2%\u0108")
        buf.write("\3\2\2\2\'\u010f\3\2\2\2)\u0114\3\2\2\2+\u0117\3\2\2\2")
        buf.write("-\u011d\3\2\2\2/\u0126\3\2\2\2\61\u012b\3\2\2\2\63\u0131")
        buf.write("\3\2\2\2\65\u0133\3\2\2\2\67\u0136\3\2\2\29\u0138\3\2")
        buf.write("\2\2;\u013b\3\2\2\2=\u013d\3\2\2\2?\u0140\3\2\2\2A\u0142")
        buf.write("\3\2\2\2C\u0145\3\2\2\2E\u0147\3\2\2\2G\u0149\3\2\2\2")
        buf.write("I\u014c\3\2\2\2K\u014f\3\2\2\2M\u0151\3\2\2\2O\u0154\3")
        buf.write("\2\2\2Q\u0157\3\2\2\2S\u0159\3\2\2\2U\u015b\3\2\2\2W\u015e")
        buf.write("\3\2\2\2Y\u0161\3\2\2\2[\u0165\3\2\2\2]\u0168\3\2\2\2")
        buf.write("_\u016b\3\2\2\2a\u016f\3\2\2\2c\u0173\3\2\2\2e\u0175\3")
        buf.write("\2\2\2g\u0177\3\2\2\2i\u0179\3\2\2\2k\u017b\3\2\2\2m\u017d")
        buf.write("\3\2\2\2o\u017f\3\2\2\2q\u0181\3\2\2\2s\u0183\3\2\2\2")
        buf.write("u\u0185\3\2\2\2w\u0187\3\2\2\2y\u0191\3\2\2\2{\u0193\3")
        buf.write("\2\2\2}\u019b\3\2\2\2\177\u01a6\3\2\2\2\u0081\u01a8\3")
        buf.write("\2\2\2\u0083\u01b1\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01c7")
        buf.write("\3\2\2\2\u0089\u01c9\3\2\2\2\u008b\u01e3\3\2\2\2\u008d")
        buf.write("\u0207\3\2\2\2\u008f\u0223\3\2\2\2\u0091\u023a\3\2\2\2")
        buf.write("\u0093\u0095\t\2\2\2\u0094\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\b\2\2\2\u0099\4\3\2\2\2\u009a\u009b")
        buf.write("\7,\2\2\u009b\u009c\7,\2\2\u009c\u00a0\3\2\2\2\u009d\u009f")
        buf.write("\13\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a3\3\2\2\2")
        buf.write("\u00a2\u00a0\3\2\2\2\u00a3\u00a4\7,\2\2\u00a4\u00a5\7")
        buf.write(",\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\b\3\2\2\u00a7\6")
        buf.write("\3\2\2\2\u00a8\u00ac\t\3\2\2\u00a9\u00ab\t\4\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\b\3\2\2\2\u00ae\u00ac\3\2\2")
        buf.write("\2\u00af\u00b0\7D\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7")
        buf.write("f\2\2\u00b2\u00b3\7{\2\2\u00b3\n\3\2\2\2\u00b4\u00b5\7")
        buf.write("G\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\f\3\2\2\2\u00b9\u00ba\7G\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7H\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\u00bf\7t\2\2\u00bf\16\3\2\2\2\u00c0\u00c1")
        buf.write("\7K\2\2\u00c1\u00c2\7h\2\2\u00c2\20\3\2\2\2\u00c3\u00c4")
        buf.write("\7X\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7t\2\2\u00c6\22")
        buf.write("\3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca\u00cb\7F\2\2\u00cb\u00cc\7q\2\2\u00cc\24")
        buf.write("\3\2\2\2\u00cd\u00ce\7D\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7m\2\2\u00d2\26")
        buf.write("\3\2\2\2\u00d3\u00d4\7G\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7u\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7K\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9\30\3\2\2\2\u00da\u00db\7G\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7f\2\2\u00dd\u00de\7Y\2\2\u00de\u00df")
        buf.write("\7j\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\7R\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7o\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7t\2\2\u00ec\34\3\2\2\2\u00ed\u00ee")
        buf.write("\7Y\2\2\u00ee\u00ef\7j\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7g\2\2\u00f2\36\3\2\2\2\u00f3\u00f4")
        buf.write("\7E\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7g\2\2\u00fb \3\2\2\2\u00fc\u00fd")
        buf.write("\7G\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7f\2\2\u00ff\u0100")
        buf.write("\7D\2\2\u0100\u0101\7q\2\2\u0101\u0102\7f\2\2\u0102\u0103")
        buf.write("\7{\2\2\u0103\"\3\2\2\2\u0104\u0105\7H\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7t\2\2\u0107$\3\2\2\2\u0108\u0109")
        buf.write("\7T\2\2\u0109\u010a\7g\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7w\2\2\u010c\u010d\7t\2\2\u010d\u010e\7p\2\2\u010e&\3")
        buf.write("\2\2\2\u010f\u0110\7V\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7w\2\2\u0112\u0113\7g\2\2\u0113(\3\2\2\2\u0114\u0115")
        buf.write("\7F\2\2\u0115\u0116\7q\2\2\u0116*\3\2\2\2\u0117\u0118")
        buf.write("\7G\2\2\u0118\u0119\7p\2\2\u0119\u011a\7f\2\2\u011a\u011b")
        buf.write("\7K\2\2\u011b\u011c\7h\2\2\u011c,\3\2\2\2\u011d\u011e")
        buf.write("\7H\2\2\u011e\u011f\7w\2\2\u011f\u0120\7p\2\2\u0120\u0121")
        buf.write("\7e\2\2\u0121\u0122\7v\2\2\u0122\u0123\7k\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7p\2\2\u0125.\3\2\2\2\u0126\u0127")
        buf.write("\7V\2\2\u0127\u0128\7j\2\2\u0128\u0129\7g\2\2\u0129\u012a")
        buf.write("\7p\2\2\u012a\60\3\2\2\2\u012b\u012c\7H\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7n\2\2\u012e\u012f\7u\2\2\u012f\u0130")
        buf.write("\7g\2\2\u0130\62\3\2\2\2\u0131\u0132\7-\2\2\u0132\64\3")
        buf.write("\2\2\2\u0133\u0134\7-\2\2\u0134\u0135\7\60\2\2\u0135\66")
        buf.write("\3\2\2\2\u0136\u0137\7/\2\2\u01378\3\2\2\2\u0138\u0139")
        buf.write("\7/\2\2\u0139\u013a\7\60\2\2\u013a:\3\2\2\2\u013b\u013c")
        buf.write("\7,\2\2\u013c<\3\2\2\2\u013d\u013e\7,\2\2\u013e\u013f")
        buf.write("\7\60\2\2\u013f>\3\2\2\2\u0140\u0141\7^\2\2\u0141@\3\2")
        buf.write("\2\2\u0142\u0143\7^\2\2\u0143\u0144\7\60\2\2\u0144B\3")
        buf.write("\2\2\2\u0145\u0146\7\'\2\2\u0146D\3\2\2\2\u0147\u0148")
        buf.write("\7#\2\2\u0148F\3\2\2\2\u0149\u014a\7(\2\2\u014a\u014b")
        buf.write("\7(\2\2\u014bH\3\2\2\2\u014c\u014d\7~\2\2\u014d\u014e")
        buf.write("\7~\2\2\u014eJ\3\2\2\2\u014f\u0150\7?\2\2\u0150L\3\2\2")
        buf.write("\2\u0151\u0152\7?\2\2\u0152\u0153\7?\2\2\u0153N\3\2\2")
        buf.write("\2\u0154\u0155\7#\2\2\u0155\u0156\7?\2\2\u0156P\3\2\2")
        buf.write("\2\u0157\u0158\7>\2\2\u0158R\3\2\2\2\u0159\u015a\7@\2")
        buf.write("\2\u015aT\3\2\2\2\u015b\u015c\7>\2\2\u015c\u015d\7?\2")
        buf.write("\2\u015dV\3\2\2\2\u015e\u015f\7@\2\2\u015f\u0160\7?\2")
        buf.write("\2\u0160X\3\2\2\2\u0161\u0162\7?\2\2\u0162\u0163\7\61")
        buf.write("\2\2\u0163\u0164\7?\2\2\u0164Z\3\2\2\2\u0165\u0166\7>")
        buf.write("\2\2\u0166\u0167\7\60\2\2\u0167\\\3\2\2\2\u0168\u0169")
        buf.write("\7@\2\2\u0169\u016a\7\60\2\2\u016a^\3\2\2\2\u016b\u016c")
        buf.write("\7>\2\2\u016c\u016d\7?\2\2\u016d\u016e\7\60\2\2\u016e")
        buf.write("`\3\2\2\2\u016f\u0170\7@\2\2\u0170\u0171\7?\2\2\u0171")
        buf.write("\u0172\7\60\2\2\u0172b\3\2\2\2\u0173\u0174\7*\2\2\u0174")
        buf.write("d\3\2\2\2\u0175\u0176\7+\2\2\u0176f\3\2\2\2\u0177\u0178")
        buf.write("\7]\2\2\u0178h\3\2\2\2\u0179\u017a\7_\2\2\u017aj\3\2\2")
        buf.write("\2\u017b\u017c\7}\2\2\u017cl\3\2\2\2\u017d\u017e\7\177")
        buf.write("\2\2\u017en\3\2\2\2\u017f\u0180\7<\2\2\u0180p\3\2\2\2")
        buf.write("\u0181\u0182\7\60\2\2\u0182r\3\2\2\2\u0183\u0184\7.\2")
        buf.write("\2\u0184t\3\2\2\2\u0185\u0186\7=\2\2\u0186v\3\2\2\2\u0187")
        buf.write("\u0188\7a\2\2\u0188x\3\2\2\2\u0189\u0192\t\5\2\2\u018a")
        buf.write("\u018e\t\6\2\2\u018b\u018d\t\5\2\2\u018c\u018b\3\2\2\2")
        buf.write("\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3")
        buf.write("\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0189")
        buf.write("\3\2\2\2\u0191\u018a\3\2\2\2\u0192z\3\2\2\2\u0193\u0194")
        buf.write("\7\62\2\2\u0194\u0198\t\7\2\2\u0195\u0197\t\b\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199|\3\2\2\2\u019a\u0198\3\2\2")
        buf.write("\2\u019b\u019c\7\62\2\2\u019c\u01a0\t\t\2\2\u019d\u019f")
        buf.write("\t\n\2\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1~\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a7\5y=\2\u01a4\u01a7\5{>\2\u01a5")
        buf.write("\u01a7\5}?\2\u01a6\u01a3\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u0080\3\2\2\2\u01a8\u01aa\t\13\2")
        buf.write("\2\u01a9\u01ab\t\f\2\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01ae\t\5\2\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u0082\3\2\2\2\u01b1\u01b5\7")
        buf.write("\60\2\2\u01b2\u01b4\t\5\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u0084\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01ba\5")
        buf.write("y=\2\u01b9\u01bb\5\u0083B\2\u01ba\u01b9\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\5\u0081")
        buf.write("A\2\u01bd\u01c4\3\2\2\2\u01be\u01bf\5y=\2\u01bf\u01c1")
        buf.write("\5\u0083B\2\u01c0\u01c2\5\u0081A\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01b8\3")
        buf.write("\2\2\2\u01c3\u01be\3\2\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c8")
        buf.write("\5\'\24\2\u01c6\u01c8\5\61\31\2\u01c7\u01c5\3\2\2\2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c8\u0088\3\2\2\2\u01c9\u01dd\7$\2\2")
        buf.write("\u01ca\u01cb\7^\2\2\u01cb\u01dc\7^\2\2\u01cc\u01cd\7^")
        buf.write("\2\2\u01cd\u01dc\7v\2\2\u01ce\u01cf\7^\2\2\u01cf\u01dc")
        buf.write("\7)\2\2\u01d0\u01d1\7^\2\2\u01d1\u01dc\7p\2\2\u01d2\u01d3")
        buf.write("\7^\2\2\u01d3\u01dc\7h\2\2\u01d4\u01d5\7^\2\2\u01d5\u01dc")
        buf.write("\7t\2\2\u01d6\u01d7\7^\2\2\u01d7\u01dc\7d\2\2\u01d8\u01d9")
        buf.write("\7)\2\2\u01d9\u01dc\7$\2\2\u01da\u01dc\n\r\2\2\u01db\u01ca")
        buf.write("\3\2\2\2\u01db\u01cc\3\2\2\2\u01db\u01ce\3\2\2\2\u01db")
        buf.write("\u01d0\3\2\2\2\u01db\u01d2\3\2\2\2\u01db\u01d4\3\2\2\2")
        buf.write("\u01db\u01d6\3\2\2\2\u01db\u01d8\3\2\2\2\u01db\u01da\3")
        buf.write("\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0")
        buf.write("\u01e1\7$\2\2\u01e1\u01e2\bE\3\2\u01e2\u008a\3\2\2\2\u01e3")
        buf.write("\u01f7\7$\2\2\u01e4\u01e5\7^\2\2\u01e5\u01f6\7^\2\2\u01e6")
        buf.write("\u01e7\7^\2\2\u01e7\u01f6\7v\2\2\u01e8\u01e9\7^\2\2\u01e9")
        buf.write("\u01f6\7)\2\2\u01ea\u01eb\7^\2\2\u01eb\u01f6\7p\2\2\u01ec")
        buf.write("\u01ed\7^\2\2\u01ed\u01f6\7h\2\2\u01ee\u01ef\7^\2\2\u01ef")
        buf.write("\u01f6\7t\2\2\u01f0\u01f1\7^\2\2\u01f1\u01f6\7d\2\2\u01f2")
        buf.write("\u01f3\7)\2\2\u01f3\u01f6\7$\2\2\u01f4\u01f6\n\16\2\2")
        buf.write("\u01f5\u01e4\3\2\2\2\u01f5\u01e6\3\2\2\2\u01f5\u01e8\3")
        buf.write("\2\2\2\u01f5\u01ea\3\2\2\2\u01f5\u01ec\3\2\2\2\u01f5\u01ee")
        buf.write("\3\2\2\2\u01f5\u01f0\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01fa\u0202\7^\2\2\u01fb\u01ff\n\17\2\2\u01fc\u01fe")
        buf.write("\n\20\2\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0203\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0202\u01fb\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\7$\2\2\u0205\u0206")
        buf.write("\bF\4\2\u0206\u008c\3\2\2\2\u0207\u021b\7$\2\2\u0208\u0209")
        buf.write("\7^\2\2\u0209\u021a\7^\2\2\u020a\u020b\7^\2\2\u020b\u021a")
        buf.write("\7v\2\2\u020c\u020d\7^\2\2\u020d\u021a\7)\2\2\u020e\u020f")
        buf.write("\7^\2\2\u020f\u021a\7p\2\2\u0210\u0211\7^\2\2\u0211\u021a")
        buf.write("\7h\2\2\u0212\u0213\7^\2\2\u0213\u021a\7t\2\2\u0214\u0215")
        buf.write("\7^\2\2\u0215\u021a\7d\2\2\u0216\u0217\7)\2\2\u0217\u021a")
        buf.write("\7$\2\2\u0218\u021a\n\r\2\2\u0219\u0208\3\2\2\2\u0219")
        buf.write("\u020a\3\2\2\2\u0219\u020c\3\2\2\2\u0219\u020e\3\2\2\2")
        buf.write("\u0219\u0210\3\2\2\2\u0219\u0212\3\2\2\2\u0219\u0214\3")
        buf.write("\2\2\2\u0219\u0216\3\2\2\2\u0219\u0218\3\2\2\2\u021a\u021d")
        buf.write("\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u0220\t\21\2")
        buf.write("\2\u021f\u021e\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221")
        buf.write("\3\2\2\2\u0221\u0222\bG\5\2\u0222\u008e\3\2\2\2\u0223")
        buf.write("\u0224\13\2\2\2\u0224\u0225\bH\6\2\u0225\u0090\3\2\2\2")
        buf.write("\u0226\u0227\7,\2\2\u0227\u0228\7,\2\2\u0228\u022c\3\2")
        buf.write("\2\2\u0229\u022b\13\2\2\2\u022a\u0229\3\2\2\2\u022b\u022e")
        buf.write("\3\2\2\2\u022c\u022d\3\2\2\2\u022c\u022a\3\2\2\2\u022d")
        buf.write("\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u023b\7,\2\2")
        buf.write("\u0230\u0231\7,\2\2\u0231\u0232\7,\2\2\u0232\u0236\3\2")
        buf.write("\2\2\u0233\u0235\13\2\2\2\u0234\u0233\3\2\2\2\u0235\u0238")
        buf.write("\3\2\2\2\u0236\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237")
        buf.write("\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023b\bI\7\2")
        buf.write("\u023a\u0226\3\2\2\2\u023a\u0230\3\2\2\2\u023b\u0092\3")
        buf.write("\2\2\2\36\2\u0096\u00a0\u00ac\u018e\u0191\u0198\u01a0")
        buf.write("\u01a6\u01aa\u01af\u01b5\u01ba\u01c1\u01c3\u01c7\u01db")
        buf.write("\u01dd\u01f5\u01f7\u01ff\u0202\u0219\u021b\u021f\u022c")
        buf.write("\u0236\u023a\b\b\2\2\3E\2\3F\3\3G\4\3H\5\3I\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    ID = 3
    BODY = 4
    ELSE = 5
    ENDFOR = 6
    IF = 7
    VAR = 8
    ENDDO = 9
    BREAK = 10
    ELSEIF = 11
    ENDWHILE = 12
    PARAMETER = 13
    WHILE = 14
    CONTINUE = 15
    ENDBODY = 16
    FOR = 17
    RETURN = 18
    TRUE = 19
    DO = 20
    ENDIF = 21
    FUNCTION = 22
    THEN = 23
    FALSE = 24
    ADDINT = 25
    ADDFLOAT = 26
    SUBINT = 27
    SUBFLOAT = 28
    MULINT = 29
    MULFLOAT = 30
    DIVINT = 31
    DIVFLOAT = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    SINGLE_EQUAL = 37
    EQUAL = 38
    NOTEQUALINT = 39
    LESSTHANINT = 40
    GREATERTHANINT = 41
    LESSEQUALINT = 42
    GREATEREQUALINT = 43
    NOTEQUALFLOAT = 44
    LESSTHANFLOAT = 45
    GREATERTHANFLOAT = 46
    LESSEQUALFLOAT = 47
    GREATEREQUALFLOAT = 48
    LRB = 49
    RRB = 50
    LSB = 51
    RSB = 52
    LB = 53
    RB = 54
    COLON = 55
    DOT = 56
    COMMA = 57
    SEMI = 58
    UNDERSCORE = 59
    INTLIT = 60
    FLOATLIT = 61
    BOOLEAN = 62
    STRING = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    ERROR_CHAR = 66
    UNTERMINATED_COMMENT = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
            "'EndIf'", "'Function'", "'Then'", "'False'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'&&'", "'||'", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "':'", "'.'", "','", "';'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "ID", "BODY", "ELSE", "ENDFOR", "IF", "VAR", 
            "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", 
            "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", 
            "FUNCTION", "THEN", "FALSE", "ADDINT", "ADDFLOAT", "SUBINT", 
            "SUBFLOAT", "MULINT", "MULFLOAT", "DIVINT", "DIVFLOAT", "MOD", 
            "NOT", "AND", "OR", "SINGLE_EQUAL", "EQUAL", "NOTEQUALINT", 
            "LESSTHANINT", "GREATERTHANINT", "LESSEQUALINT", "GREATEREQUALINT", 
            "NOTEQUALFLOAT", "LESSTHANFLOAT", "GREATERTHANFLOAT", "LESSEQUALFLOAT", 
            "GREATEREQUALFLOAT", "LRB", "RRB", "LSB", "RSB", "LB", "RB", 
            "COLON", "DOT", "COMMA", "SEMI", "UNDERSCORE", "INTLIT", "FLOATLIT", 
            "BOOLEAN", "STRING", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "WS", "COMMENT", "ID", "BODY", "ELSE", "ENDFOR", "IF", 
                  "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
                  "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", 
                  "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "ADDINT", 
                  "ADDFLOAT", "SUBINT", "SUBFLOAT", "MULINT", "MULFLOAT", 
                  "DIVINT", "DIVFLOAT", "MOD", "NOT", "AND", "OR", "SINGLE_EQUAL", 
                  "EQUAL", "NOTEQUALINT", "LESSTHANINT", "GREATERTHANINT", 
                  "LESSEQUALINT", "GREATEREQUALINT", "NOTEQUALFLOAT", "LESSTHANFLOAT", 
                  "GREATERTHANFLOAT", "LESSEQUALFLOAT", "GREATEREQUALFLOAT", 
                  "LRB", "RRB", "LSB", "RSB", "LB", "RB", "COLON", "DOT", 
                  "COMMA", "SEMI", "UNDERSCORE", "DEC", "HEX", "OCT", "INTLIT", 
                  "EXP", "Decimal", "FLOATLIT", "BOOLEAN", "STRING", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text=self.text[1:-1]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

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
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise UncloseString(self.text[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text[0:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise UnterminatedComment()
                
     


