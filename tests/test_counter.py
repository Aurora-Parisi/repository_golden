from lib.counter import Counter

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
