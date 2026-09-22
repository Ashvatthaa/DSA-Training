# DSA Training in Python

A collection of classroom exercises and home assignments for learning data structures and algorithms with Python. The repository follows a day-by-day progression from basic array operations to two-pointer, hashing, prefix-sum, sliding-window, and maximum-subarray techniques.

## Repository Structure

```text
class/       Classroom demonstrations and guided practice
Home-task/   Practice problems and take-home exercises
```

Most files are standalone scripts. Run a file with:

```bash
python "path/to/file.py"
```

Some scripts read input from the terminal; others use sample arrays defined in the file.

## Topics Covered

- Basic statistics: averages, minimum and maximum values, and score analysis
- Number sequences: Fibonacci and attendance-style problems
- Arrays: searching, reversing, rotating, rearranging, and sorting checks
- Strings and characters: ASCII conversion and repeated or unique characters
- Hashing and frequency counting: duplicates, occurrences, and common elements
- Two-pointer techniques: pair, 3Sum, 4Sum, and sorted-array problems
- Prefix sums and sliding windows: subarray sums, averages, distinct elements, and window maximums
- Greedy and dynamic programming fundamentals: stock profit and Kadane's algorithm
- Time and space complexity: several exercises include complexity analysis

## Exercise Index

### Classroom Practice

| Day | Exercise | Main concept |
| --- | --- | --- |
| 1 | [average.py](class/day-1/average.py) | Average of array values |
| 1 | [average_min_max.py](class/day-1/average_min_max.py) | Minimum and maximum in one pass |
| 1 | [first_second_largest.py](class/day-1/first_second_largest.py) | First and second largest values |
| 2 | [attendance.py](class/day-2/attendance.py) | Attendance processing |
| 2 | [attendance(without).py](class/day-2/attendance%28without%29.py) | Attendance processing without a helper approach |
| 2 | [fibo.py](class/day-2/fibo.py) | Fibonacci sequence |
| 2 | [Fibonacci.py](class/day-2/Fibonacci.py) | Fibonacci implementation |
| 3 | [fibo_space_complexity.py](class/day-3/fibo_space_complexity.py) | Fibonacci and space complexity |
| 4 | [1_first_last_occurance_two_pointer.py](class/day-4/1_first_last_occurance_two_pointer.py) | First and last occurrence with two pointers |
| 4 | [2_reverse_array.py](class/day-4/2_reverse_array.py) | Array reversal |
| 4 | [3_reverse_array_two_pointer.py](class/day-4/3_reverse_array_two_pointer.py) | In-place reversal with two pointers |
| 4 | [4_rotate_array_left.py](class/day-4/4_rotate_array_left.py) | Left rotation |
| 4 | [5_rotate_array_right_negative_indexing.py](class/day-4/5_rotate_array_right_negative_indexing.py) | Right rotation with negative indexing |
| 5 | [1_ascii_character_value_conversion.py](class/day-5/1_ascii_character_value_conversion.py) | ASCII and character conversion |
| 5 | [first_occurance_search_removal_shift.py](class/day-5/first_occurance_search_removal_shift.py) | Search, remove, and shift elements |
| 6 | [contains_duplicate.py](class/day-6/contains_duplicate.py) | Duplicate detection |
| 6 | [count_freq_of_every_element.py](class/day-6/count_freq_of_every_element.py) | Frequency counting |
| 6 | [non_repeating_element.py](class/day-6/non_repeating_element.py) | Finding a non-repeating element |
| 7 | [max_value_so_far.py](class/day-7/max_value_so_far.py) | Running maximum |
| 7 | [range_min_max.py](class/day-7/range_min_max.py) | Minimum and maximum in a range |
| 7 | [weather_station_min.py](class/day-7/weather_station_min.py) | Minimum temperature/value tracking |
| 8 | [1_two_sum.py](class/day-8/1_two_sum.py) | Two Sum |
| 8 | [1572.Matrix_diagonal_sum.py](class/day-8/1572.Matrix_diagonal_sum.py) | Matrix diagonal sum |
| 8 | [167.Two_sum_II-Input_array_is_sorted.py](class/day-8/167.Two_sum_II-Input_array_is_sorted.py) | Two Sum II on a sorted array |
| 9 | [Kadanes_algorithm.py](class/day-9/Kadanes_algorithm.py) | Maximum subarray sum |
| 9 | [maxsum_eachwindow.py](class/day-9/maxsum_eachwindow.py) | Maximum sum for a fixed window |
| 9 | [two_pointers.py](class/day-9/two_pointers.py) | Two-pointer array technique |

### Home Tasks

| Day | Exercise | Main concept |
| --- | --- | --- |
| 1 | [to_learn.py](Home-task/day-1/to_learn.py) | Introductory Python/DSA practice |
| 2 | [employees.py](Home-task/day-2/employees.py) | Employee data processing |
| 2 | [employees1.py](Home-task/day-2/employees1.py) | Employee data processing variation |
| 2 | [employees2.py](Home-task/day-2/employees2.py) | Employee data processing variation |
| 3 | [1_exam_score_statistics.py](Home-task/day-3/1_exam_score_statistics.py) | Exam score statistics |
| 3 | [2_placement_cutoff.py](Home-task/day-3/2_placement_cutoff.py) | Placement cutoff calculation |
| 3 | [3_first_last_occurance.py](Home-task/day-3/3_first_last_occurance.py) | First and last occurrence |
| 3 | [4_reverse_studentid.py](Home-task/day-3/4_reverse_studentid.py) | Reversing a student ID |
| 3 | [5_print_all_pairs.py](Home-task/day-3/5_print_all_pairs.py) | Generating all pairs |
| 4 | [1_right_rotation_positive_indexing.py](Home-task/day-4/1_right_rotation_positive_indexing.py) | Right rotation with positive indexing |
| 4 | [2_left_rotation_reverse_algorithm.py](Home-task/day-4/2_left_rotation_reverse_algorithm.py) | Left rotation with the reversal algorithm |
| 4 | [3_rearrange_positive_negative_numbers.py](Home-task/day-4/3_rearrange_positive_negative_numbers.py) | Positive and negative rearrangement |
| 4 | [4_reorder_array_using_index.py](Home-task/day-4/4_reorder_array_using_index.py) | Reordering by index |
| 4 | [5_reverse_array_single_pointer.py](Home-task/day-4/5_reverse_array_single_pointer.py) | Reversal with a single pointer |
| 4 | [6_rearrange_array_alternately.py](Home-task/day-4/6_rearrange_array_alternately.py) | Alternating array rearrangement |
| 4 | [7_rearrange_array_arr_i_equals_i.py](Home-task/day-4/7_rearrange_array_arr_i_equals_i.py) | Place values at matching indices |
| 4 | [8_rearrange_array_o1_extra_space.py](Home-task/day-4/8_rearrange_array_o1_extra_space.py) | In-place rearrangement with $O(1)$ extra space |
| 5 | [1_moving_zeroes.py](Home-task/day-5/1_moving_zeroes.py) | Moving zeroes to the end |
| 5 | [2_check_if_array_is_sorted.py](Home-task/day-5/2_check_if_array_is_sorted.py) | Checking whether an array is sorted |
| 6 | [1207_Unique_NumberofOccurances.py](Home-task/day-6/1207_Unique_NumberofOccurances.py) | Unique number of occurrences |
| 6 | [1748_SumofUniqueElements.py](Home-task/day-6/1748_SumofUniqueElements.py) | Sum of unique elements |
| 6 | [219_ContainsDuplicates.py](Home-task/day-6/219_ContainsDuplicates.py) | Contains Duplicate |
| 6 | [2956_FindCommonElementsBetweenTwoArrays.py](Home-task/day-6/2956_FindCommonElementsBetweenTwoArrays.py) | Common elements between arrays |
| 6 | [442-FindAllDuplicatesArray.py](Home-task/day-6/442-FindAllDuplicatesArray.py) | Find all duplicates |
| 7 | [12_BestTimeToBuyAndSellStock.py](Home-task/day-7/12_BestTimeToBuyAndSellStock.py) | Best time to buy and sell stock |
| 7 | [387_FirstUniqueCharacter_In_a_String.py](Home-task/day-7/387_FirstUniqueCharacter_In_a_String.py) | First unique character |
| 7 | [First_Repeated_Character.py](Home-task/day-7/First_Repeated_Character.py) | First repeated character |
| 8 | [15_3sum.py](Home-task/day-8/15_3sum.py) | 3Sum with two pointers |
| 8 | [18_4sum.py](Home-task/day-8/18_4sum.py) | 4Sum |
| 8 | [Max_pair_sum_less_than_k.py](Home-task/day-8/Max_pair_sum_less_than_k.py) | Maximum pair sum below a limit |
| 9 | [count_distinct.py](Home-task/day-9/count_distinct.py) | Distinct values in a window/range |
| 9 | [maxsum_subarrays(2461).py](Home-task/day-9/maxsum_subarrays%282461%29.py) | Maximum sum of a subarray with constraints |
| 9 | [no_of_subarrays.py](Home-task/day-9/no_of_subarrays.py) | Counting subarrays |
| 9 | [prefix_avg.py](Home-task/day-9/prefix_avg.py) | Prefix averages |
| 9 | [slidingwindow_max(239).py](Home-task/day-9/slidingwindow_max%28239%29.py) | Sliding Window Maximum |

## Progression

| Stage | Days | Focus |
| --- | --- | --- |
| Foundations | 1-3 | Loops, statistics, sequences, and complexity |
| Array manipulation | 4-5 | Searching, reversing, rotating, and rearranging |
| Hashing and strings | 6-7 | Frequencies, duplicates, uniqueness, and greedy scans |
| Problem-solving patterns | 8-9 | Two pointers, prefix sums, sliding windows, and subarray problems |

## Notes

- File names are preserved as they appear in the repository, including spaces, parentheses, dots, and capitalization.
- The exercises are intended for practice and may use hard-coded sample data or interactive input.
- When extending the repository, place guided examples under `class/day-X/` and independent practice under `Home-task/day-X/`.
