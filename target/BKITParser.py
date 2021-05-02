# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0223\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\5\2j\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3r\n\3\3\4\3\4")
        buf.write("\5\4v\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u0082\n\6\3\7\3\7\5\7\u0086\n\7\3\b\3\b\3\b\5\b\u008b")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0095\n\t\3\n")
        buf.write("\3\n\3\n\5\n\u009a\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u00a3\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ab")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b3\n\r\3\r\3\r\3\r")
        buf.write("\5\r\u00b8\n\r\3\r\5\r\u00bb\n\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00c5\n\16\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00cb\n\17\3\20\3\20\3\20\3\20\5\20\u00d1\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00dd")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u00e6\n")
        buf.write("\23\3\24\5\24\u00e9\n\24\3\24\5\24\u00ec\n\24\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00f2\n\25\3\25\5\25\u00f5\n\25\3\25\5")
        buf.write("\25\u00f8\n\25\3\25\5\25\u00fb\n\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0104\n\26\3\26\5\26\u0107\n\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\5\26\u010f\n\26\3\26\5\26")
        buf.write("\u0112\n\26\5\26\u0114\n\26\3\27\3\27\5\27\u0118\n\27")
        buf.write("\3\27\5\27\u011b\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\5\30\u0129\n\30\3\30\5\30")
        buf.write("\u012c\n\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\5!\u0150\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0181")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u018c\n#\f#\16#\u018f")
        buf.write("\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u01a0")
        buf.write("\n$\f$\16$\u01a3\13$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\7%\u01b7\n%\f%\16%\u01ba\13%\3&")
        buf.write("\3&\3&\5&\u01bf\n&\3\'\3\'\3\'\3\'\3\'\5\'\u01c6\n\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\5(\u01cf\n(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\5)\u01d9\n)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01e7")
        buf.write("\n+\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01f5\n-\3")
        buf.write(".\3.\5.\u01f9\n.\3/\3/\3/\5/\u01fe\n/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u0207\n\60\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u020d\n\61\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u0215")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\7\64\u021e\n")
        buf.write("\64\f\64\16\64\u0221\13\64\3\64\2\5DFH\65\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdf\2\2\2\u0249\2i\3\2\2\2\4q\3\2\2\2")
        buf.write("\6u\3\2\2\2\bw\3\2\2\2\n\u0081\3\2\2\2\f\u0085\3\2\2\2")
        buf.write("\16\u008a\3\2\2\2\20\u0094\3\2\2\2\22\u0099\3\2\2\2\24")
        buf.write("\u00a2\3\2\2\2\26\u00aa\3\2\2\2\30\u00ac\3\2\2\2\32\u00c4")
        buf.write("\3\2\2\2\34\u00ca\3\2\2\2\36\u00d0\3\2\2\2 \u00dc\3\2")
        buf.write("\2\2\"\u00de\3\2\2\2$\u00e5\3\2\2\2&\u00e8\3\2\2\2(\u00ed")
        buf.write("\3\2\2\2*\u0113\3\2\2\2,\u0115\3\2\2\2.\u011c\3\2\2\2")
        buf.write("\60\u0130\3\2\2\2\62\u0132\3\2\2\2\64\u0134\3\2\2\2\66")
        buf.write("\u0136\3\2\2\28\u013d\3\2\2\2:\u0144\3\2\2\2<\u0147\3")
        buf.write("\2\2\2>\u014a\3\2\2\2@\u014d\3\2\2\2B\u0180\3\2\2\2D\u0182")
        buf.write("\3\2\2\2F\u0190\3\2\2\2H\u01a4\3\2\2\2J\u01be\3\2\2\2")
        buf.write("L\u01c5\3\2\2\2N\u01ce\3\2\2\2P\u01d8\3\2\2\2R\u01da\3")
        buf.write("\2\2\2T\u01e6\3\2\2\2V\u01e8\3\2\2\2X\u01f4\3\2\2\2Z\u01f8")
        buf.write("\3\2\2\2\\\u01fa\3\2\2\2^\u0206\3\2\2\2`\u0208\3\2\2\2")
        buf.write("b\u0214\3\2\2\2d\u0216\3\2\2\2f\u021a\3\2\2\2hj\5\4\3")
        buf.write("\2ih\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2")
        buf.write("mn\5\6\4\2no\5\4\3\2or\3\2\2\2pr\5\6\4\2qm\3\2\2\2qp\3")
        buf.write("\2\2\2r\5\3\2\2\2sv\5\b\5\2tv\5\30\r\2us\3\2\2\2ut\3\2")
        buf.write("\2\2v\7\3\2\2\2wx\7\n\2\2xy\79\2\2yz\5\n\6\2z{\7<\2\2")
        buf.write("{\t\3\2\2\2|}\5\f\7\2}~\7;\2\2~\177\5\n\6\2\177\u0082")
        buf.write("\3\2\2\2\u0080\u0082\5\f\7\2\u0081|\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\13\3\2\2\2\u0083\u0086\5\20\t\2\u0084\u0086")
        buf.write("\5\16\b\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\r\3\2\2\2\u0087\u008b\7\5\2\2\u0088\u0089\7\5\2\2\u0089")
        buf.write("\u008b\5\24\13\2\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2")
        buf.write("\2\u008b\17\3\2\2\2\u008c\u008d\7\5\2\2\u008d\u008e\7")
        buf.write("\'\2\2\u008e\u0095\5\26\f\2\u008f\u0090\7\5\2\2\u0090")
        buf.write("\u0091\5\24\13\2\u0091\u0092\7\'\2\2\u0092\u0093\5`\61")
        buf.write("\2\u0093\u0095\3\2\2\2\u0094\u008c\3\2\2\2\u0094\u008f")
        buf.write("\3\2\2\2\u0095\21\3\2\2\2\u0096\u009a\7\5\2\2\u0097\u0098")
        buf.write("\7\5\2\2\u0098\u009a\5\24\13\2\u0099\u0096\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\23\3\2\2\2\u009b\u009c\7\65\2\2\u009c")
        buf.write("\u009d\7>\2\2\u009d\u009e\7\66\2\2\u009e\u00a3\5\24\13")
        buf.write("\2\u009f\u00a0\7\65\2\2\u00a0\u00a1\7>\2\2\u00a1\u00a3")
        buf.write("\7\66\2\2\u00a2\u009b\3\2\2\2\u00a2\u009f\3\2\2\2\u00a3")
        buf.write("\25\3\2\2\2\u00a4\u00ab\7>\2\2\u00a5\u00ab\7?\2\2\u00a6")
        buf.write("\u00ab\7\25\2\2\u00a7\u00ab\7\32\2\2\u00a8\u00ab\7A\2")
        buf.write("\2\u00a9\u00ab\5d\63\2\u00aa\u00a4\3\2\2\2\u00aa\u00a5")
        buf.write("\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\27\3\2\2\2\u00ac")
        buf.write("\u00ad\7\30\2\2\u00ad\u00ae\79\2\2\u00ae\u00b2\7\5\2\2")
        buf.write("\u00af\u00b0\7\17\2\2\u00b0\u00b1\79\2\2\u00b1\u00b3\5")
        buf.write("\32\16\2\u00b2\u00af\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b5\7\6\2\2\u00b5\u00b7\79\2\2")
        buf.write("\u00b6\u00b8\5\34\17\2\u00b7\u00b6\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00bb\5\36\20\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00bd\7\22\2\2\u00bd\u00be\7:\2\2\u00be\31\3\2")
        buf.write("\2\2\u00bf\u00c0\5\16\b\2\u00c0\u00c1\7;\2\2\u00c1\u00c2")
        buf.write("\5\32\16\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5\16\b\2\u00c4")
        buf.write("\u00bf\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\33\3\2\2\2\u00c6")
        buf.write("\u00c7\5\b\5\2\u00c7\u00c8\5\34\17\2\u00c8\u00cb\3\2\2")
        buf.write("\2\u00c9\u00cb\5\b\5\2\u00ca\u00c6\3\2\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00cb\35\3\2\2\2\u00cc\u00cd\5 \21\2\u00cd\u00ce")
        buf.write("\5\36\20\2\u00ce\u00d1\3\2\2\2\u00cf\u00d1\5 \21\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\37\3\2\2\2\u00d2")
        buf.write("\u00dd\5\"\22\2\u00d3\u00dd\5(\25\2\u00d4\u00dd\5.\30")
        buf.write("\2\u00d5\u00dd\5\66\34\2\u00d6\u00dd\58\35\2\u00d7\u00dd")
        buf.write("\5:\36\2\u00d8\u00dd\5<\37\2\u00d9\u00dd\5> \2\u00da\u00dd")
        buf.write("\5@!\2\u00db\u00dd\5\b\5\2\u00dc\u00d2\3\2\2\2\u00dc\u00d3")
        buf.write("\3\2\2\2\u00dc\u00d4\3\2\2\2\u00dc\u00d5\3\2\2\2\u00dc")
        buf.write("\u00d6\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dc\u00d8\3\2\2\2")
        buf.write("\u00dc\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3")
        buf.write("\2\2\2\u00dd!\3\2\2\2\u00de\u00df\5$\23\2\u00df\u00e0")
        buf.write("\7\'\2\2\u00e0\u00e1\5B\"\2\u00e1\u00e2\7<\2\2\u00e2#")
        buf.write("\3\2\2\2\u00e3\u00e6\7\5\2\2\u00e4\u00e6\5V,\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6%\3\2\2\2\u00e7\u00e9")
        buf.write("\5\34\17\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00eb\3\2\2\2\u00ea\u00ec\5\36\20\2\u00eb\u00ea\3\2\2")
        buf.write("\2\u00eb\u00ec\3\2\2\2\u00ec\'\3\2\2\2\u00ed\u00ee\7\t")
        buf.write("\2\2\u00ee\u00ef\5B\"\2\u00ef\u00f1\7\31\2\2\u00f0\u00f2")
        buf.write("\5\34\17\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f4\3\2\2\2\u00f3\u00f5\5\36\20\2\u00f4\u00f3\3\2\2")
        buf.write("\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00f8")
        buf.write("\5*\26\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00fa\3\2\2\2\u00f9\u00fb\5,\27\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7")
        buf.write("\27\2\2\u00fd\u00fe\7:\2\2\u00fe)\3\2\2\2\u00ff\u0100")
        buf.write("\7\r\2\2\u0100\u0101\5B\"\2\u0101\u0103\7\31\2\2\u0102")
        buf.write("\u0104\5\34\17\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2")
        buf.write("\2\u0104\u0106\3\2\2\2\u0105\u0107\5\36\20\2\u0106\u0105")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\5*\26\2\u0109\u0114\3\2\2\2\u010a\u010b\7\r\2\2")
        buf.write("\u010b\u010c\5B\"\2\u010c\u010e\7\31\2\2\u010d\u010f\5")
        buf.write("\34\17\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u0112\5\36\20\2\u0111\u0110\3\2\2")
        buf.write("\2\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u00ff")
        buf.write("\3\2\2\2\u0113\u010a\3\2\2\2\u0114+\3\2\2\2\u0115\u0117")
        buf.write("\7\7\2\2\u0116\u0118\5\34\17\2\u0117\u0116\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u011b\5\36\20")
        buf.write("\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b-\3\2")
        buf.write("\2\2\u011c\u011d\7\23\2\2\u011d\u011e\7\63\2\2\u011e\u011f")
        buf.write("\7\5\2\2\u011f\u0120\7\'\2\2\u0120\u0121\5\60\31\2\u0121")
        buf.write("\u0122\7;\2\2\u0122\u0123\5\62\32\2\u0123\u0124\7;\2\2")
        buf.write("\u0124\u0125\5\64\33\2\u0125\u0126\7\64\2\2\u0126\u0128")
        buf.write("\7\26\2\2\u0127\u0129\5\34\17\2\u0128\u0127\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u012c\5\36\20")
        buf.write("\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012e\7\b\2\2\u012e\u012f\7:\2\2\u012f")
        buf.write("/\3\2\2\2\u0130\u0131\5B\"\2\u0131\61\3\2\2\2\u0132\u0133")
        buf.write("\5B\"\2\u0133\63\3\2\2\2\u0134\u0135\5B\"\2\u0135\65\3")
        buf.write("\2\2\2\u0136\u0137\7\20\2\2\u0137\u0138\5B\"\2\u0138\u0139")
        buf.write("\7\26\2\2\u0139\u013a\5&\24\2\u013a\u013b\7\16\2\2\u013b")
        buf.write("\u013c\7:\2\2\u013c\67\3\2\2\2\u013d\u013e\7\26\2\2\u013e")
        buf.write("\u013f\5&\24\2\u013f\u0140\7\20\2\2\u0140\u0141\5B\"\2")
        buf.write("\u0141\u0142\7\13\2\2\u0142\u0143\7:\2\2\u01439\3\2\2")
        buf.write("\2\u0144\u0145\7\f\2\2\u0145\u0146\7<\2\2\u0146;\3\2\2")
        buf.write("\2\u0147\u0148\7\21\2\2\u0148\u0149\7<\2\2\u0149=\3\2")
        buf.write("\2\2\u014a\u014b\5\\/\2\u014b\u014c\7<\2\2\u014c?\3\2")
        buf.write("\2\2\u014d\u014f\7\24\2\2\u014e\u0150\5B\"\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\7<\2\2\u0152A\3\2\2\2\u0153\u0154\5D#\2\u0154\u0155")
        buf.write("\7(\2\2\u0155\u0156\5D#\2\u0156\u0181\3\2\2\2\u0157\u0158")
        buf.write("\5D#\2\u0158\u0159\7)\2\2\u0159\u015a\5D#\2\u015a\u0181")
        buf.write("\3\2\2\2\u015b\u015c\5D#\2\u015c\u015d\7*\2\2\u015d\u015e")
        buf.write("\5D#\2\u015e\u0181\3\2\2\2\u015f\u0160\5D#\2\u0160\u0161")
        buf.write("\7+\2\2\u0161\u0162\5D#\2\u0162\u0181\3\2\2\2\u0163\u0164")
        buf.write("\5D#\2\u0164\u0165\7,\2\2\u0165\u0166\5D#\2\u0166\u0181")
        buf.write("\3\2\2\2\u0167\u0168\5D#\2\u0168\u0169\7-\2\2\u0169\u016a")
        buf.write("\5D#\2\u016a\u0181\3\2\2\2\u016b\u016c\5D#\2\u016c\u016d")
        buf.write("\7.\2\2\u016d\u016e\5D#\2\u016e\u0181\3\2\2\2\u016f\u0170")
        buf.write("\5D#\2\u0170\u0171\7/\2\2\u0171\u0172\5D#\2\u0172\u0181")
        buf.write("\3\2\2\2\u0173\u0174\5D#\2\u0174\u0175\7\60\2\2\u0175")
        buf.write("\u0176\5D#\2\u0176\u0181\3\2\2\2\u0177\u0178\5D#\2\u0178")
        buf.write("\u0179\7\61\2\2\u0179\u017a\5D#\2\u017a\u0181\3\2\2\2")
        buf.write("\u017b\u017c\5D#\2\u017c\u017d\7\62\2\2\u017d\u017e\5")
        buf.write("D#\2\u017e\u0181\3\2\2\2\u017f\u0181\5D#\2\u0180\u0153")
        buf.write("\3\2\2\2\u0180\u0157\3\2\2\2\u0180\u015b\3\2\2\2\u0180")
        buf.write("\u015f\3\2\2\2\u0180\u0163\3\2\2\2\u0180\u0167\3\2\2\2")
        buf.write("\u0180\u016b\3\2\2\2\u0180\u016f\3\2\2\2\u0180\u0173\3")
        buf.write("\2\2\2\u0180\u0177\3\2\2\2\u0180\u017b\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181C\3\2\2\2\u0182\u0183\b#\1\2\u0183\u0184")
        buf.write("\5F$\2\u0184\u018d\3\2\2\2\u0185\u0186\f\5\2\2\u0186\u0187")
        buf.write("\7%\2\2\u0187\u018c\5F$\2\u0188\u0189\f\4\2\2\u0189\u018a")
        buf.write("\7&\2\2\u018a\u018c\5F$\2\u018b\u0185\3\2\2\2\u018b\u0188")
        buf.write("\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018eE\3\2\2\2\u018f\u018d\3\2\2\2\u0190")
        buf.write("\u0191\b$\1\2\u0191\u0192\5H%\2\u0192\u01a1\3\2\2\2\u0193")
        buf.write("\u0194\f\7\2\2\u0194\u0195\7\33\2\2\u0195\u01a0\5H%\2")
        buf.write("\u0196\u0197\f\6\2\2\u0197\u0198\7\34\2\2\u0198\u01a0")
        buf.write("\5H%\2\u0199\u019a\f\5\2\2\u019a\u019b\7\35\2\2\u019b")
        buf.write("\u01a0\5H%\2\u019c\u019d\f\4\2\2\u019d\u019e\7\36\2\2")
        buf.write("\u019e\u01a0\5H%\2\u019f\u0193\3\2\2\2\u019f\u0196\3\2")
        buf.write("\2\2\u019f\u0199\3\2\2\2\u019f\u019c\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("G\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b%\1\2\u01a5")
        buf.write("\u01a6\5J&\2\u01a6\u01b8\3\2\2\2\u01a7\u01a8\f\b\2\2\u01a8")
        buf.write("\u01a9\7\37\2\2\u01a9\u01b7\5J&\2\u01aa\u01ab\f\7\2\2")
        buf.write("\u01ab\u01ac\7 \2\2\u01ac\u01b7\5J&\2\u01ad\u01ae\f\6")
        buf.write("\2\2\u01ae\u01af\7!\2\2\u01af\u01b7\5J&\2\u01b0\u01b1")
        buf.write("\f\5\2\2\u01b1\u01b2\7\"\2\2\u01b2\u01b7\5J&\2\u01b3\u01b4")
        buf.write("\f\4\2\2\u01b4\u01b5\7#\2\2\u01b5\u01b7\5J&\2\u01b6\u01a7")
        buf.write("\3\2\2\2\u01b6\u01aa\3\2\2\2\u01b6\u01ad\3\2\2\2\u01b6")
        buf.write("\u01b0\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b7\u01ba\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9I\3\2\2")
        buf.write("\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7$\2\2\u01bc\u01bf")
        buf.write("\5J&\2\u01bd\u01bf\5L\'\2\u01be\u01bb\3\2\2\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bfK\3\2\2\2\u01c0\u01c1\7\36\2\2\u01c1\u01c6")
        buf.write("\5L\'\2\u01c2\u01c3\7\35\2\2\u01c3\u01c6\5L\'\2\u01c4")
        buf.write("\u01c6\5N(\2\u01c5\u01c0\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6M\3\2\2\2\u01c7\u01cf\5P)\2\u01c8")
        buf.write("\u01c9\7\63\2\2\u01c9\u01ca\5B\"\2\u01ca\u01cb\7\64\2")
        buf.write("\2\u01cb\u01cf\3\2\2\2\u01cc\u01cf\5V,\2\u01cd\u01cf\5")
        buf.write("\\/\2\u01ce\u01c7\3\2\2\2\u01ce\u01c8\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cfO\3\2\2\2\u01d0\u01d9")
        buf.write("\7\5\2\2\u01d1\u01d9\7>\2\2\u01d2\u01d9\7?\2\2\u01d3\u01d9")
        buf.write("\7\25\2\2\u01d4\u01d9\7\32\2\2\u01d5\u01d9\7A\2\2\u01d6")
        buf.write("\u01d9\5R*\2\u01d7\u01d9\5`\61\2\u01d8\u01d0\3\2\2\2\u01d8")
        buf.write("\u01d1\3\2\2\2\u01d8\u01d2\3\2\2\2\u01d8\u01d3\3\2\2\2")
        buf.write("\u01d8\u01d4\3\2\2\2\u01d8\u01d5\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d8\u01d7\3\2\2\2\u01d9Q\3\2\2\2\u01da\u01db")
        buf.write("\7\5\2\2\u01db\u01dc\5T+\2\u01dcS\3\2\2\2\u01dd\u01de")
        buf.write("\7\65\2\2\u01de\u01df\5B\"\2\u01df\u01e0\7\66\2\2\u01e0")
        buf.write("\u01e1\5T+\2\u01e1\u01e7\3\2\2\2\u01e2\u01e3\7\65\2\2")
        buf.write("\u01e3\u01e4\5B\"\2\u01e4\u01e5\7\66\2\2\u01e5\u01e7\3")
        buf.write("\2\2\2\u01e6\u01dd\3\2\2\2\u01e6\u01e2\3\2\2\2\u01e7U")
        buf.write("\3\2\2\2\u01e8\u01e9\5Z.\2\u01e9\u01ea\5X-\2\u01eaW\3")
        buf.write("\2\2\2\u01eb\u01ec\7\65\2\2\u01ec\u01ed\5B\"\2\u01ed\u01ee")
        buf.write("\7\66\2\2\u01ee\u01f5\3\2\2\2\u01ef\u01f0\7\65\2\2\u01f0")
        buf.write("\u01f1\5B\"\2\u01f1\u01f2\7\66\2\2\u01f2\u01f3\5X-\2\u01f3")
        buf.write("\u01f5\3\2\2\2\u01f4\u01eb\3\2\2\2\u01f4\u01ef\3\2\2\2")
        buf.write("\u01f5Y\3\2\2\2\u01f6\u01f9\7\5\2\2\u01f7\u01f9\5\\/\2")
        buf.write("\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9[\3\2\2")
        buf.write("\2\u01fa\u01fb\7\5\2\2\u01fb\u01fd\7\63\2\2\u01fc\u01fe")
        buf.write("\5^\60\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0200\7\64\2\2\u0200]\3\2\2\2\u0201")
        buf.write("\u0202\5B\"\2\u0202\u0203\7;\2\2\u0203\u0204\5^\60\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0207\5B\"\2\u0206\u0201\3\2\2\2")
        buf.write("\u0206\u0205\3\2\2\2\u0207_\3\2\2\2\u0208\u020c\7\67\2")
        buf.write("\2\u0209\u020d\5f\64\2\u020a\u020d\5d\63\2\u020b\u020d")
        buf.write("\5b\62\2\u020c\u0209\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\78\2\2")
        buf.write("\u020fa\3\2\2\2\u0210\u0211\5d\63\2\u0211\u0212\5b\62")
        buf.write("\2\u0212\u0215\3\2\2\2\u0213\u0215\5d\63\2\u0214\u0210")
        buf.write("\3\2\2\2\u0214\u0213\3\2\2\2\u0215c\3\2\2\2\u0216\u0217")
        buf.write("\7\67\2\2\u0217\u0218\5f\64\2\u0218\u0219\78\2\2\u0219")
        buf.write("e\3\2\2\2\u021a\u021f\5\26\f\2\u021b\u021c\7;\2\2\u021c")
        buf.write("\u021e\5\26\f\2\u021d\u021b\3\2\2\2\u021e\u0221\3\2\2")
        buf.write("\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220g\3\2")
        buf.write("\2\2\u0221\u021f\3\2\2\2\67iqu\u0081\u0085\u008a\u0094")
        buf.write("\u0099\u00a2\u00aa\u00b2\u00b7\u00ba\u00c4\u00ca\u00d0")
        buf.write("\u00dc\u00e5\u00e8\u00eb\u00f1\u00f4\u00f7\u00fa\u0103")
        buf.write("\u0106\u010e\u0111\u0113\u0117\u011a\u0128\u012b\u014f")
        buf.write("\u0180\u018b\u018d\u019f\u01a1\u01b6\u01b8\u01be\u01c5")
        buf.write("\u01ce\u01d8\u01e6\u01f4\u01f8\u01fd\u0206\u020c\u0214")
        buf.write("\u021f")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
                     "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", 
                     "'While'", "'Continue'", "'EndBody'", "'For'", "'Return'", 
                     "'True'", "'Do'", "'EndIf'", "'Function'", "'Then'", 
                     "'False'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "':'", "'.'", "','", "';'", "'_'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "ID", "BODY", "ELSE", 
                      "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", 
                      "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", 
                      "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", 
                      "THEN", "FALSE", "ADDINT", "ADDFLOAT", "SUBINT", "SUBFLOAT", 
                      "MULINT", "MULFLOAT", "DIVINT", "DIVFLOAT", "MOD", 
                      "NOT", "AND", "OR", "SINGLE_EQUAL", "EQUAL", "NOTEQUALINT", 
                      "LESSTHANINT", "GREATERTHANINT", "LESSEQUALINT", "GREATEREQUALINT", 
                      "NOTEQUALFLOAT", "LESSTHANFLOAT", "GREATERTHANFLOAT", 
                      "LESSEQUALFLOAT", "GREATEREQUALFLOAT", "LRB", "RRB", 
                      "LSB", "RSB", "LB", "RB", "COLON", "DOT", "COMMA", 
                      "SEMI", "UNDERSCORE", "INTLIT", "FLOATLIT", "BOOLEAN", 
                      "STRING", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_manydeclaration = 1
    RULE_declarations = 2
    RULE_var_declarations = 3
    RULE_variable_list = 4
    RULE_var_part = 5
    RULE_un_init_var = 6
    RULE_init_var = 7
    RULE_var_name = 8
    RULE_dimension = 9
    RULE_normal_literals = 10
    RULE_main_statement = 11
    RULE_parameter_list = 12
    RULE_var_body = 13
    RULE_statement_lists = 14
    RULE_statement_list = 15
    RULE_assign_statement = 16
    RULE_lhs = 17
    RULE_body_part = 18
    RULE_if_statement = 19
    RULE_elseif_part = 20
    RULE_else_part = 21
    RULE_for_statement = 22
    RULE_init_exp = 23
    RULE_condition_exp = 24
    RULE_update_exp = 25
    RULE_while_statement = 26
    RULE_do_while_statement = 27
    RULE_break_statement = 28
    RULE_continue_statement = 29
    RULE_call_statement = 30
    RULE_return_statement = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_exp6 = 38
    RULE_literals = 39
    RULE_array_name = 40
    RULE_dimen = 41
    RULE_index_expression = 42
    RULE_index_operator = 43
    RULE_index_expression_name = 44
    RULE_function_call = 45
    RULE_argument_list = 46
    RULE_array_literal = 47
    RULE_many_array = 48
    RULE_one_array = 49
    RULE_array_value = 50

    ruleNames =  [ "program", "manydeclaration", "declarations", "var_declarations", 
                   "variable_list", "var_part", "un_init_var", "init_var", 
                   "var_name", "dimension", "normal_literals", "main_statement", 
                   "parameter_list", "var_body", "statement_lists", "statement_list", 
                   "assign_statement", "lhs", "body_part", "if_statement", 
                   "elseif_part", "else_part", "for_statement", "init_exp", 
                   "condition_exp", "update_exp", "while_statement", "do_while_statement", 
                   "break_statement", "continue_statement", "call_statement", 
                   "return_statement", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "literals", "array_name", "dimen", "index_expression", 
                   "index_operator", "index_expression_name", "function_call", 
                   "argument_list", "array_literal", "many_array", "one_array", 
                   "array_value" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    ID=3
    BODY=4
    ELSE=5
    ENDFOR=6
    IF=7
    VAR=8
    ENDDO=9
    BREAK=10
    ELSEIF=11
    ENDWHILE=12
    PARAMETER=13
    WHILE=14
    CONTINUE=15
    ENDBODY=16
    FOR=17
    RETURN=18
    TRUE=19
    DO=20
    ENDIF=21
    FUNCTION=22
    THEN=23
    FALSE=24
    ADDINT=25
    ADDFLOAT=26
    SUBINT=27
    SUBFLOAT=28
    MULINT=29
    MULFLOAT=30
    DIVINT=31
    DIVFLOAT=32
    MOD=33
    NOT=34
    AND=35
    OR=36
    SINGLE_EQUAL=37
    EQUAL=38
    NOTEQUALINT=39
    LESSTHANINT=40
    GREATERTHANINT=41
    LESSEQUALINT=42
    GREATEREQUALINT=43
    NOTEQUALFLOAT=44
    LESSTHANFLOAT=45
    GREATERTHANFLOAT=46
    LESSEQUALFLOAT=47
    GREATEREQUALFLOAT=48
    LRB=49
    RRB=50
    LSB=51
    RSB=52
    LB=53
    RB=54
    COLON=55
    DOT=56
    COMMA=57
    SEMI=58
    UNDERSCORE=59
    INTLIT=60
    FLOATLIT=61
    BOOLEAN=62
    STRING=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    ERROR_CHAR=66
    UNTERMINATED_COMMENT=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def manydeclaration(self):
            return self.getTypedRuleContext(BKITParser.ManydeclarationContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR or _la==BKITParser.FUNCTION:
                self.state = 102
                self.manydeclaration()


            self.state = 105
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarations(self):
            return self.getTypedRuleContext(BKITParser.DeclarationsContext,0)


        def manydeclaration(self):
            return self.getTypedRuleContext(BKITParser.ManydeclarationContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_manydeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManydeclaration" ):
                return visitor.visitManydeclaration(self)
            else:
                return visitor.visitChildren(self)




    def manydeclaration(self):

        localctx = BKITParser.ManydeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydeclaration)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.declarations()
                self.state = 108
                self.manydeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.declarations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declarations(self):
            return self.getTypedRuleContext(BKITParser.Var_declarationsContext,0)


        def main_statement(self):
            return self.getTypedRuleContext(BKITParser.Main_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = BKITParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declarations)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.var_declarations()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.main_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declarations" ):
                return visitor.visitVar_declarations(self)
            else:
                return visitor.visitChildren(self)




    def var_declarations(self):

        localctx = BKITParser.Var_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BKITParser.VAR)
            self.state = 118
            self.match(BKITParser.COLON)
            self.state = 119
            self.variable_list()
            self.state = 120
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_part(self):
            return self.getTypedRuleContext(BKITParser.Var_partContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_list)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.var_part()
                self.state = 123
                self.match(BKITParser.COMMA)
                self.state = 124
                self.variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.var_part()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_var(self):
            return self.getTypedRuleContext(BKITParser.Init_varContext,0)


        def un_init_var(self):
            return self.getTypedRuleContext(BKITParser.Un_init_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_part" ):
                return visitor.visitVar_part(self)
            else:
                return visitor.visitChildren(self)




    def var_part(self):

        localctx = BKITParser.Var_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_part)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.init_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.un_init_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Un_init_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_un_init_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUn_init_var" ):
                return visitor.visitUn_init_var(self)
            else:
                return visitor.visitChildren(self)




    def un_init_var(self):

        localctx = BKITParser.Un_init_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_un_init_var)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(BKITParser.ID)
                self.state = 135
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SINGLE_EQUAL(self):
            return self.getToken(BKITParser.SINGLE_EQUAL, 0)

        def normal_literals(self):
            return self.getTypedRuleContext(BKITParser.Normal_literalsContext,0)


        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(BKITParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_var" ):
                return visitor.visitInit_var(self)
            else:
                return visitor.visitChildren(self)




    def init_var(self):

        localctx = BKITParser.Init_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_init_var)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(BKITParser.ID)
                self.state = 139
                self.match(BKITParser.SINGLE_EQUAL)
                self.state = 140
                self.normal_literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(BKITParser.ID)
                self.state = 142
                self.dimension()
                self.state = 143
                self.match(BKITParser.SINGLE_EQUAL)
                self.state = 144
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_name" ):
                return visitor.visitVar_name(self)
            else:
                return visitor.visitChildren(self)




    def var_name(self):

        localctx = BKITParser.Var_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_name)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(BKITParser.ID)
                self.state = 150
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dimension)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(BKITParser.LSB)
                self.state = 154
                self.match(BKITParser.INTLIT)
                self.state = 155
                self.match(BKITParser.RSB)
                self.state = 156
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(BKITParser.LSB)
                self.state = 158
                self.match(BKITParser.INTLIT)
                self.state = 159
                self.match(BKITParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_literalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def one_array(self):
            return self.getTypedRuleContext(BKITParser.One_arrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_normal_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_literals" ):
                return visitor.visitNormal_literals(self)
            else:
                return visitor.visitChildren(self)




    def normal_literals(self):

        localctx = BKITParser.Normal_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_normal_literals)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(BKITParser.TRUE)
                pass
            elif token in [BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(BKITParser.FALSE)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.one_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_main_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_statement" ):
                return visitor.visitMain_statement(self)
            else:
                return visitor.visitChildren(self)




    def main_statement(self):

        localctx = BKITParser.Main_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_main_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BKITParser.FUNCTION)
            self.state = 171
            self.match(BKITParser.COLON)
            self.state = 172
            self.match(BKITParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 173
                self.match(BKITParser.PARAMETER)
                self.state = 174
                self.match(BKITParser.COLON)
                self.state = 175
                self.parameter_list()


            self.state = 178
            self.match(BKITParser.BODY)
            self.state = 179
            self.match(BKITParser.COLON)
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 180
                self.var_body()


            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.VAR) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 183
                self.statement_lists()


            self.state = 186
            self.match(BKITParser.ENDBODY)
            self.state = 187
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def un_init_var(self):
            return self.getTypedRuleContext(BKITParser.Un_init_varContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = BKITParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_list)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.un_init_var()
                self.state = 190
                self.match(BKITParser.COMMA)
                self.state = 191
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.un_init_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declarations(self):
            return self.getTypedRuleContext(BKITParser.Var_declarationsContext,0)


        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_body" ):
                return visitor.visitVar_body(self)
            else:
                return visitor.visitChildren(self)




    def var_body(self):

        localctx = BKITParser.Var_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_body)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.var_declarations()
                self.state = 197
                self.var_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.var_declarations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_lists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_lists" ):
                return visitor.visitStatement_lists(self)
            else:
                return visitor.visitChildren(self)




    def statement_lists(self):

        localctx = BKITParser.Statement_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement_lists)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.statement_list()
                self.state = 203
                self.statement_lists()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.statement_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(BKITParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKITParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKITParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BKITParser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(BKITParser.Do_while_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKITParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKITParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(BKITParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKITParser.Return_statementContext,0)


        def var_declarations(self):
            return self.getTypedRuleContext(BKITParser.Var_declarationsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement_list)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.do_while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 215
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 216
                self.return_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 217
                self.var_declarations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKITParser.LhsContext,0)


        def SINGLE_EQUAL(self):
            return self.getToken(BKITParser.SINGLE_EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = BKITParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.lhs()
            self.state = 221
            self.match(BKITParser.SINGLE_EQUAL)
            self.state = 222
            self.exp()
            self.state = 223
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_expression(self):
            return self.getTypedRuleContext(BKITParser.Index_expressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKITParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lhs)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.index_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_part" ):
                return visitor.visitBody_part(self)
            else:
                return visitor.visitChildren(self)




    def body_part(self):

        localctx = BKITParser.Body_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_body_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 229
                self.var_body()


            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 232
                self.statement_lists()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def elseif_part(self):
            return self.getTypedRuleContext(BKITParser.Elseif_partContext,0)


        def else_part(self):
            return self.getTypedRuleContext(BKITParser.Else_partContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(BKITParser.IF)
            self.state = 236
            self.exp()
            self.state = 237
            self.match(BKITParser.THEN)
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 238
                self.var_body()


            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.VAR) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 241
                self.statement_lists()


            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 244
                self.elseif_part()


            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 247
                self.else_part()


            self.state = 250
            self.match(BKITParser.ENDIF)
            self.state = 251
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def elseif_part(self):
            return self.getTypedRuleContext(BKITParser.Elseif_partContext,0)


        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_part" ):
                return visitor.visitElseif_part(self)
            else:
                return visitor.visitChildren(self)




    def elseif_part(self):

        localctx = BKITParser.Elseif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elseif_part)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(BKITParser.ELSEIF)
                self.state = 254
                self.exp()
                self.state = 255
                self.match(BKITParser.THEN)
                self.state = 257
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 256
                    self.var_body()


                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.VAR) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                    self.state = 259
                    self.statement_lists()


                self.state = 262
                self.elseif_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(BKITParser.ELSEIF)
                self.state = 265
                self.exp()
                self.state = 266
                self.match(BKITParser.THEN)
                self.state = 268
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 267
                    self.var_body()


                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.VAR) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                    self.state = 270
                    self.statement_lists()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = BKITParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKITParser.ELSE)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 276
                self.var_body()


            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.VAR) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 279
                self.statement_lists()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LRB(self):
            return self.getToken(BKITParser.LRB, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SINGLE_EQUAL(self):
            return self.getToken(BKITParser.SINGLE_EQUAL, 0)

        def init_exp(self):
            return self.getTypedRuleContext(BKITParser.Init_expContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def condition_exp(self):
            return self.getTypedRuleContext(BKITParser.Condition_expContext,0)


        def update_exp(self):
            return self.getTypedRuleContext(BKITParser.Update_expContext,0)


        def RRB(self):
            return self.getToken(BKITParser.RRB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_body(self):
            return self.getTypedRuleContext(BKITParser.Var_bodyContext,0)


        def statement_lists(self):
            return self.getTypedRuleContext(BKITParser.Statement_listsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKITParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(BKITParser.FOR)
            self.state = 283
            self.match(BKITParser.LRB)
            self.state = 284
            self.match(BKITParser.ID)
            self.state = 285
            self.match(BKITParser.SINGLE_EQUAL)
            self.state = 286
            self.init_exp()
            self.state = 287
            self.match(BKITParser.COMMA)
            self.state = 288
            self.condition_exp()
            self.state = 289
            self.match(BKITParser.COMMA)
            self.state = 290
            self.update_exp()
            self.state = 291
            self.match(BKITParser.RRB)
            self.state = 292
            self.match(BKITParser.DO)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 293
                self.var_body()


            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.VAR) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 296
                self.statement_lists()


            self.state = 299
            self.match(BKITParser.ENDFOR)
            self.state = 300
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_exp" ):
                return visitor.visitInit_exp(self)
            else:
                return visitor.visitChildren(self)




    def init_exp(self):

        localctx = BKITParser.Init_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_init_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_condition_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_exp" ):
                return visitor.visitCondition_exp(self)
            else:
                return visitor.visitChildren(self)




    def condition_exp(self):

        localctx = BKITParser.Condition_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condition_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_update_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_exp" ):
                return visitor.visitUpdate_exp(self)
            else:
                return visitor.visitChildren(self)




    def update_exp(self):

        localctx = BKITParser.Update_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_update_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def body_part(self):
            return self.getTypedRuleContext(BKITParser.Body_partContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = BKITParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(BKITParser.WHILE)
            self.state = 309
            self.exp()
            self.state = 310
            self.match(BKITParser.DO)
            self.state = 311
            self.body_part()
            self.state = 312
            self.match(BKITParser.ENDWHILE)
            self.state = 313
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def body_part(self):
            return self.getTypedRuleContext(BKITParser.Body_partContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = BKITParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKITParser.DO)
            self.state = 316
            self.body_part()
            self.state = 317
            self.match(BKITParser.WHILE)
            self.state = 318
            self.exp()
            self.state = 319
            self.match(BKITParser.ENDDO)
            self.state = 320
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(BKITParser.BREAK)
            self.state = 323
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BKITParser.CONTINUE)
            self.state = 326
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = BKITParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.function_call()
            self.state = 329
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(BKITParser.RETURN)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUBINT) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LRB) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRING))) != 0):
                self.state = 332
                self.exp()


            self.state = 335
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOTEQUALINT(self):
            return self.getToken(BKITParser.NOTEQUALINT, 0)

        def LESSTHANINT(self):
            return self.getToken(BKITParser.LESSTHANINT, 0)

        def GREATERTHANINT(self):
            return self.getToken(BKITParser.GREATERTHANINT, 0)

        def LESSEQUALINT(self):
            return self.getToken(BKITParser.LESSEQUALINT, 0)

        def GREATEREQUALINT(self):
            return self.getToken(BKITParser.GREATEREQUALINT, 0)

        def NOTEQUALFLOAT(self):
            return self.getToken(BKITParser.NOTEQUALFLOAT, 0)

        def LESSTHANFLOAT(self):
            return self.getToken(BKITParser.LESSTHANFLOAT, 0)

        def GREATERTHANFLOAT(self):
            return self.getToken(BKITParser.GREATERTHANFLOAT, 0)

        def LESSEQUALFLOAT(self):
            return self.getToken(BKITParser.LESSEQUALFLOAT, 0)

        def GREATEREQUALFLOAT(self):
            return self.getToken(BKITParser.GREATEREQUALFLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.exp1(0)
                self.state = 338
                self.match(BKITParser.EQUAL)
                self.state = 339
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.exp1(0)
                self.state = 342
                self.match(BKITParser.NOTEQUALINT)
                self.state = 343
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.exp1(0)
                self.state = 346
                self.match(BKITParser.LESSTHANINT)
                self.state = 347
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.exp1(0)
                self.state = 350
                self.match(BKITParser.GREATERTHANINT)
                self.state = 351
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 353
                self.exp1(0)
                self.state = 354
                self.match(BKITParser.LESSEQUALINT)
                self.state = 355
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 357
                self.exp1(0)
                self.state = 358
                self.match(BKITParser.GREATEREQUALINT)
                self.state = 359
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 361
                self.exp1(0)
                self.state = 362
                self.match(BKITParser.NOTEQUALFLOAT)
                self.state = 363
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 365
                self.exp1(0)
                self.state = 366
                self.match(BKITParser.LESSTHANFLOAT)
                self.state = 367
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 369
                self.exp1(0)
                self.state = 370
                self.match(BKITParser.GREATERTHANFLOAT)
                self.state = 371
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 373
                self.exp1(0)
                self.state = 374
                self.match(BKITParser.LESSEQUALFLOAT)
                self.state = 375
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 377
                self.exp1(0)
                self.state = 378
                self.match(BKITParser.GREATEREQUALFLOAT)
                self.state = 379
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 381
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 393
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 387
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 388
                        self.match(BKITParser.AND)
                        self.state = 389
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 390
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 391
                        self.match(BKITParser.OR)
                        self.state = 392
                        self.exp2(0)
                        pass

             
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADDINT(self):
            return self.getToken(BKITParser.ADDINT, 0)

        def ADDFLOAT(self):
            return self.getToken(BKITParser.ADDFLOAT, 0)

        def SUBINT(self):
            return self.getToken(BKITParser.SUBINT, 0)

        def SUBFLOAT(self):
            return self.getToken(BKITParser.SUBFLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 413
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 401
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 402
                        self.match(BKITParser.ADDINT)
                        self.state = 403
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 404
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 405
                        self.match(BKITParser.ADDFLOAT)
                        self.state = 406
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 407
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 408
                        self.match(BKITParser.SUBINT)
                        self.state = 409
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 410
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 411
                        self.match(BKITParser.SUBFLOAT)
                        self.state = 412
                        self.exp3(0)
                        pass

             
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MULINT(self):
            return self.getToken(BKITParser.MULINT, 0)

        def MULFLOAT(self):
            return self.getToken(BKITParser.MULFLOAT, 0)

        def DIVINT(self):
            return self.getToken(BKITParser.DIVINT, 0)

        def DIVFLOAT(self):
            return self.getToken(BKITParser.DIVFLOAT, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 436
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 421
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 422
                        self.match(BKITParser.MULINT)
                        self.state = 423
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 424
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 425
                        self.match(BKITParser.MULFLOAT)
                        self.state = 426
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 427
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 428
                        self.match(BKITParser.DIVINT)
                        self.state = 429
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 430
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 431
                        self.match(BKITParser.DIVFLOAT)
                        self.state = 432
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 433
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 434
                        self.match(BKITParser.MOD)
                        self.state = 435
                        self.exp4()
                        pass

             
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp4)
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(BKITParser.NOT)
                self.state = 442
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUBINT, BKITParser.SUBFLOAT, BKITParser.LRB, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBFLOAT(self):
            return self.getToken(BKITParser.SUBFLOAT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUBINT(self):
            return self.getToken(BKITParser.SUBINT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp5)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUBFLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(BKITParser.SUBFLOAT)
                self.state = 447
                self.exp5()
                pass
            elif token in [BKITParser.SUBINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(BKITParser.SUBINT)
                self.state = 449
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LRB, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 450
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext,0)


        def LRB(self):
            return self.getToken(BKITParser.LRB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RRB(self):
            return self.getToken(BKITParser.RRB, 0)

        def index_expression(self):
            return self.getTypedRuleContext(BKITParser.Index_expressionContext,0)


        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp6)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.match(BKITParser.LRB)
                self.state = 455
                self.exp()
                self.state = 456
                self.match(BKITParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.index_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 459
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def array_name(self):
            return self.getTypedRuleContext(BKITParser.Array_nameContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(BKITParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKITParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literals)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(BKITParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.match(BKITParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 465
                self.match(BKITParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 466
                self.match(BKITParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 467
                self.match(BKITParser.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 468
                self.array_name()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 469
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimen(self):
            return self.getTypedRuleContext(BKITParser.DimenContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_name" ):
                return visitor.visitArray_name(self)
            else:
                return visitor.visitChildren(self)




    def array_name(self):

        localctx = BKITParser.Array_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(BKITParser.ID)
            self.state = 473
            self.dimen()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def dimen(self):
            return self.getTypedRuleContext(BKITParser.DimenContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimen" ):
                return visitor.visitDimen(self)
            else:
                return visitor.visitChildren(self)




    def dimen(self):

        localctx = BKITParser.DimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_dimen)
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(BKITParser.LSB)
                self.state = 476
                self.exp()
                self.state = 477
                self.match(BKITParser.RSB)
                self.state = 478
                self.dimen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(BKITParser.LSB)
                self.state = 481
                self.exp()
                self.state = 482
                self.match(BKITParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expression_name(self):
            return self.getTypedRuleContext(BKITParser.Index_expression_nameContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)




    def index_expression(self):

        localctx = BKITParser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_index_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.index_expression_name()
            self.state = 487
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_index_operator)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(BKITParser.LSB)
                self.state = 490
                self.exp()
                self.state = 491
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.match(BKITParser.LSB)
                self.state = 494
                self.exp()
                self.state = 495
                self.match(BKITParser.RSB)
                self.state = 496
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expression_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_expression_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression_name" ):
                return visitor.visitIndex_expression_name(self)
            else:
                return visitor.visitChildren(self)




    def index_expression_name(self):

        localctx = BKITParser.Index_expression_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_index_expression_name)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LRB(self):
            return self.getToken(BKITParser.LRB, 0)

        def RRB(self):
            return self.getToken(BKITParser.RRB, 0)

        def argument_list(self):
            return self.getTypedRuleContext(BKITParser.Argument_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(BKITParser.ID)
            self.state = 505
            self.match(BKITParser.LRB)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUBINT) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LRB) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRING))) != 0):
                self.state = 506
                self.argument_list()


            self.state = 509
            self.match(BKITParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def argument_list(self):
            return self.getTypedRuleContext(BKITParser.Argument_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = BKITParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_argument_list)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.exp()
                self.state = 512
                self.match(BKITParser.COMMA)
                self.state = 513
                self.argument_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def array_value(self):
            return self.getTypedRuleContext(BKITParser.Array_valueContext,0)


        def one_array(self):
            return self.getTypedRuleContext(BKITParser.One_arrayContext,0)


        def many_array(self):
            return self.getTypedRuleContext(BKITParser.Many_arrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = BKITParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(BKITParser.LB)
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 519
                self.array_value()
                pass

            elif la_ == 2:
                self.state = 520
                self.one_array()
                pass

            elif la_ == 3:
                self.state = 521
                self.many_array()
                pass


            self.state = 524
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_array(self):
            return self.getTypedRuleContext(BKITParser.One_arrayContext,0)


        def many_array(self):
            return self.getTypedRuleContext(BKITParser.Many_arrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_array" ):
                return visitor.visitMany_array(self)
            else:
                return visitor.visitChildren(self)




    def many_array(self):

        localctx = BKITParser.Many_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_many_array)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.one_array()
                self.state = 527
                self.many_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.one_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def array_value(self):
            return self.getTypedRuleContext(BKITParser.Array_valueContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_one_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_array" ):
                return visitor.visitOne_array(self)
            else:
                return visitor.visitChildren(self)




    def one_array(self):

        localctx = BKITParser.One_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_one_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(BKITParser.LB)
            self.state = 533
            self.array_value()
            self.state = 534
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_literals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Normal_literalsContext)
            else:
                return self.getTypedRuleContext(BKITParser.Normal_literalsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = BKITParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.normal_literals()
            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 537
                self.match(BKITParser.COMMA)
                self.state = 538
                self.normal_literals()
                self.state = 543
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.exp1_sempred
        self._predicates[34] = self.exp2_sempred
        self._predicates[35] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




