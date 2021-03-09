from csv_combiner import process, get_headers, scan_files


def test_process_success():
    want = "A, B, x.csv"
    got = process("A, B", "x.csv")
    assert got == want


def test_get_headers_success():
    want = "email_hash, category, filename"
    got = get_headers("./fixtures/clothing.csv")
    assert want == got


def test_get_headers_unknown_file():
    want = False
    got = get_headers("./fixtures/unknown.csv")
    assert want == got