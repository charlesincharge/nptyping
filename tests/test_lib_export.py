from unittest import TestCase

from nptyping import __all__


class LibExportTest(TestCase):
    def test_all(self):
        expected_exports = {
            "NDArray",
            "RecArray",
            "assert_isinstance",
            "validate_shape_expression",
            "normalize_shape_expression",
            "NPTypingError",
            "InvalidDTypeError",
            "InvalidShapeError",
            "InvalidStructureError",
            "InvalidArgumentsError",
            "Shape",
            "Structure",
            "__version__",
            "DType",
            "Number",
            "Bool",
            "Bool8",
            "Object",
            "Object0",
            "Datetime64",
            "Integer",
            "SignedInteger",
            "Int8",
            "Int16",
            "Int32",
            "Int64",
            "Byte",
            "Short",
            "IntC",
            "IntP",
            "Int0",
            "Int",
            "LongLong",
            "Timedelta64",
            "UnsignedInteger",
            "UInt8",
            "UInt16",
            "UInt32",
            "UInt64",
            "UByte",
            "UShort",
            "UIntC",
            "UIntP",
            "UInt0",
            "UInt",
            "ULongLong",
            "Inexact",
            "Floating",
            "Float16",
            "Float32",
            "Float64",
            "Half",
            "Single",
            "Double",
            "Float",
            "LongDouble",
            "LongFloat",
            "ComplexFloating",
            "Complex64",
            "Complex128",
            "CSingle",
            "SingleComplex",
            "CDouble",
            "Complex",
            "CFloat",
            "CLongDouble",
            "CLongFloat",
            "LongComplex",
            "Flexible",
            "Void",
            "Void0",
            "Character",
            "Bytes",
            "String",
            "Bytes0",
            "Unicode",
            "Str0",
            "DataFrame",
        }

        self.assertSetEqual(expected_exports, set(__all__))
