class WALSegmentCleaner:
    """
    LSM/Distributed WAL Segment Cleaner with Tombstone Compaction.
    Merges active and immutable log segments, eliminating overwritten keys and deleted records.
    """
    def __init__(self):
        self.segments = []

    def add_segment(self, segment_records):
        self.segments.append(dict(segment_records))

    def compact(self):
        merged = {}
        for seg in self.segments:
            for k, (val, is_tombstone) in seg.items():
                if is_tombstone:
                    merged.pop(k, None)
                else:
                    merged[k] = val
        self.segments = [{k: (v, False) for k, v in merged.items()}]
        return merged
