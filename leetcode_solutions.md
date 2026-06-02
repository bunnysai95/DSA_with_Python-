# LeetCode Solutions Tracker

> Tip: Press **Ctrl+Shift+V** in VS Code to open the rendered Markdown preview (shows the table as a real grid).

## Progress Table

| No. | Problem | Difficulty | Topic | Pattern / Approach | Time | Space | Status | Revisit? |
|-----|---------|------------|-------|--------------------|------|-------|--------|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array / Hash Map | Hash map one-pass | O(n) | O(n) | ✅ Solved | No |
| 2 |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |

---

## Detailed Solutions

### 1. Two Sum  `Easy`
**Link:** https://leetcode.com/problems/two-sum/
**Topic:** Array / Hash Map
**Pattern:** Hash map one-pass

**Intuition:**
Store each number's index in a hash map as you iterate. For every number, check
if `target - num` was already seen. If yes, you found the pair.

**Complexity:** Time `O(n)` · Space `O(n)`

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
```

**Notes:** Brute force is O(n²); the hash map trades space for speed.

---

<!-- Copy the block below for each new problem -->
<!--
### N. Problem Name  `Difficulty`
**Link:**
**Topic:**
**Pattern:**

**Intuition:**


**Complexity:** Time `O()` · Space `O()`

```python

```

**Notes:**

---
-->
