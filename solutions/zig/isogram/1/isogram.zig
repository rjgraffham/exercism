pub fn isIsogram(str: []const u8) bool {
    var seen: [26]bool = [_]bool{false} ** 26;

    for (str) |char| {
        if (char >= 'A' and char <= 'Z') {
            if (seen[char - 'A']) {
                return false;
            } else {
                seen[char - 'A'] = true;
            }
        } else if (char >= 'a' and char <= 'z') {
            if (seen[char - 'a']) {
                return false;
            } else {
                seen[char - 'a'] = true;
            }
        }
    }

    // We looped over the whole string without seeing a letter we'd seen before
    return true;
}
