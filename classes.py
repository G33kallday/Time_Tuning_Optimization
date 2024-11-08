class Note:
    def __init__(self,name,cents):
        self.name = name
        self.cents = cents


class Interval:
    def __init__(self,lower_note,higher_note,just_cents_diff):
        self.lower_note = lower_note
        self.higher_note = higher_note
        self.just_cents_diff = just_cents_diff

        interval_in_cents = self.higher_note.cents - self.lower_note.cents

        if interval_in_cents < 0:
            interval_in_cents +=1200
            self.interval_in_cents = interval_in_cents
        else:
            self.interval_in_cents = interval_in_cents


