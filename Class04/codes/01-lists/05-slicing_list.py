from prettytable import PrettyTable

"""
SLICING A LIST
    Syntax: <list_name>[start : end : step]

    where:
        -> start (optional): Index to begin the slice (inclusive - included). 
            Defaults to 0 if omitted
        -> end (optional): Index to end the slice (exclusive - excluded). 
            Defaults to the length of the list if omitted
        -> step (optional): Step size, specifying the interval between elements. 
            Defaults to 1 if omitted
"""

# ========== PART 1 - NEW LIST ==========
sample_list = list()
sample_list.extend(["new_element", True, 65.87 - 9.17j, "upGrad", None, "1", 5])
sample_list_class = type(sample_list)
sample_list_class_name = sample_list_class.__name__
sample_list_id = id(sample_list)
sample_list_len = len(sample_list)

# ========== PART 2 - SLICING LIST ==========
## (2.1) GET ALL ITEMS
sample_list_all_elements = sample_list[:]
sample_list_all_elements_class = type(sample_list_all_elements)
sample_list_all_elements_class_name = sample_list_all_elements_class.__name__
sample_list_all_elements_id = id(sample_list_all_elements)
sample_list_all_elements_len = len(sample_list_all_elements)

## (2.2) GET ALL ITEMS AFTER A SPECIFIC POSITION (INCLUDE START POSITION)
start_position = 2
sample_list_after_pos2 = sample_list[start_position:]
sample_list_after_pos2_class = type(sample_list_after_pos2)
sample_list_after_pos2_class_name = sample_list_after_pos2_class.__name__
sample_list_after_pos2_id = id(sample_list_after_pos2)
sample_list_after_pos2_len = len(sample_list_after_pos2)

## (2.3) GET ALL ITEMS BEFORE A SPECIFIC POSITION (EXCLUDE END POSITION)
end_position = 3
sample_list_before_pos3 = sample_list[:end_position]
sample_list_before_pos3_class = type(sample_list_before_pos3)
sample_list_before_pos3_class_name = sample_list_before_pos3_class.__name__
sample_list_before_pos3_id = id(sample_list_before_pos3)
sample_list_before_pos3_len = len(sample_list_before_pos3)

## (2.4) GET ALL ITEMS BETWEEN 2 POSITIONS (EXCLUDE END POSITION)
start_position = 1
end_position = 4
sample_list_pos1_pos4 = sample_list[start_position:end_position]
sample_list_pos1_pos4_class = type(sample_list_pos1_pos4)
sample_list_pos1_pos4_class_name = sample_list_pos1_pos4_class.__name__
sample_list_pos1_pos4_id = id(sample_list_pos1_pos4)
sample_list_pos1_pos4_len = len(sample_list_pos1_pos4)

## (2.5) GET ITEMS AT SPECIFIED INTERVALS
step = 2
sample_list_step2 = sample_list[::step]
sample_list_step2_class = type(sample_list_step2)
sample_list_step2_class_name = sample_list_step2_class.__name__
sample_list_step2_id = id(sample_list_step2)
sample_list_step2_len = len(sample_list_step2)

## (2.6) OUT-OF-BOUND SLICING (EXCLUDE END POSITION AND USES THE LIST LEN LIMIT)
start_position = 5
end_position = 10
sample_list_pos5_pos10 = sample_list[start_position:end_position]
sample_list_pos5_pos10_class = type(sample_list_pos5_pos10)
sample_list_pos5_pos10_class_name = sample_list_pos5_pos10_class.__name__
sample_list_pos5_pos10_id = id(sample_list_pos5_pos10)
sample_list_pos5_pos10_len = len(sample_list_pos5_pos10)

## (2.7) EXTRACT ELEMENTS USING NEGATIVE INDEXES
start_position = -4
end_position = -1
sample_list_neg4_neg1 = sample_list[start_position:end_position]
sample_list_neg4_neg1_class = type(sample_list_neg4_neg1)
sample_list_neg4_neg1_class_name = sample_list_neg4_neg1_class.__name__
sample_list_neg4_neg1_id = id(sample_list_neg4_neg1)
sample_list_neg4_neg1_len = len(sample_list_neg4_neg1)

## (2.8) REVERSE A LIST USING SLICING
step = -1
sample_list_step_neg1 = sample_list[::step]
sample_list_step_neg1_class = type(sample_list_step_neg1)
sample_list_step_neg1_class_name = sample_list_step_neg1_class.__name__
sample_list_step_neg1_id = id(sample_list_step_neg1)
sample_list_step_neg1_len = len(sample_list_step_neg1)


# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['NEW LIST', sample_list, sample_list_class, sample_list_class_name, sample_list_id, sample_list_len])

table.add_row(['=========', '=========', '=========', '=========', '=========', '========='])
table.add_row(['SLICING LIST', '', '', '', '', ''])
table.add_row(["Slice all", sample_list_all_elements, sample_list_all_elements_class,
               sample_list_all_elements_class_name, sample_list_all_elements_id, sample_list_all_elements_len])
table.add_row(["Slice after position 2", sample_list_after_pos2, sample_list_after_pos2_class,
               sample_list_after_pos2_class_name, sample_list_after_pos2_id, sample_list_after_pos2_len])
table.add_row(["Slice before position 3", sample_list_before_pos3, sample_list_before_pos3_class,
               sample_list_before_pos3_class_name, sample_list_before_pos3_id, sample_list_before_pos3_len])
table.add_row(["Slice position 1 to 4", sample_list_pos1_pos4, sample_list_pos1_pos4_class,
               sample_list_pos1_pos4_class_name, sample_list_pos1_pos4_id, sample_list_pos1_pos4_len])
table.add_row(["Slice all step 2", sample_list_step2, sample_list_step2_class, sample_list_step2_class_name,
               sample_list_step2_id, sample_list_step2_len])
table.add_row(["Slice out of bound (5 to 10)", sample_list_pos5_pos10, sample_list_pos5_pos10_class,
               sample_list_pos5_pos10_class_name, sample_list_pos5_pos10_id, sample_list_pos5_pos10_len])
table.add_row(["Slice position -4 to -1", sample_list_neg4_neg1, sample_list_neg4_neg1_class,
               sample_list_neg4_neg1_class_name, sample_list_neg4_neg1_id, sample_list_neg4_neg1_len])
table.add_row(["Slice reverse list", sample_list_step_neg1, sample_list_step_neg1_class,
               sample_list_step_neg1_class_name, sample_list_step_neg1_id, sample_list_step_neg1_len])
print(table)