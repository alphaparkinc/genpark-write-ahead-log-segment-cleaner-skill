from client import WALSegmentCleaner

def main():
    print("=== Testing WAL Segment Cleaner with Tombstone Compaction ===")
    cleaner = WALSegmentCleaner()

    # Segment 1: initial writes
    cleaner.add_segment({"record_1": ("v1", False), "record_2": ("v2", False)})
    # Segment 2: update record_1, delete record_2 via tombstone
    cleaner.add_segment({"record_1": ("v1_updated", False), "record_2": ("", True)})
    # Segment 3: new insert
    cleaner.add_segment({"record_3": ("v3", False)})

    print(f"Total uncompacted segments: {len(cleaner.segments)}")
    compacted = cleaner.compact()
    print("Compacted records:", compacted)
    assert compacted == {"record_1": "v1_updated", "record_3": "v3"}
    assert "record_2" not in compacted
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
