STATE_SIZE = 1600
BLOCK_SIZE = 1024
CAPACITY = STATE_SIZE - BLOCK_SIZE
LANE_SIZE = 64
rate_lanes = BLOCK_SIZE // LANE_SIZE
capacity_lanes = CAPACITY // LANE_SIZE

print("State Size      :", STATE_SIZE, "bits")
print("Block Size      :", BLOCK_SIZE, "bits")
print("Capacity        :", CAPACITY, "bits")
print("Rate Lanes      :", rate_lanes)
print("Capacity Lanes  :", capacity_lanes)

blocks = 0
remaining = capacity_lanes

while remaining > 0:
    blocks += 1

    changed = min(rate_lanes, remaining)
    remaining -= changed

    print("\nAfter Message Block", blocks)
    print("Nonzero Capacity Lanes:",
          capacity_lanes - remaining,
          "/", capacity_lanes)

print("\nAll capacity lanes become nonzero after",
      blocks, "message block(s).")