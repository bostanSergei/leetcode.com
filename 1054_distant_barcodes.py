def rearrangeBarcodes(barcodes: list) -> list:
    barcode_dict = {}
    for num in barcodes:
        if num not in barcode_dict:
            barcode_dict[num] = 0
        barcode_dict[num] += 1

    repeat_list = sorted(barcode_dict.items(), key=lambda tpl: tpl[1], reverse=True)

    result_list = [None] * (l := len(barcodes))
    index = 0

    for elem, count in repeat_list:
        for i in range(count):
            result_list[index] = elem

            if index == l - 1 or index == l - 2:
                index = 1
            else:
                index += 2
    return result_list


barcodes = [1, 1, 1, 1, 2, 2, 3, 3]
print(rearrangeBarcodes(barcodes))
