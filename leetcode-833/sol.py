class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        acc = 0
        rt = s
        for tp in sorted(zip(indices, sources, targets)):
            index, source, target = tp
            end_index = index + len(source)
            subst = s[index:end_index]
            if subst == source:
                fix_bgn_idx = index + acc
                end_index += acc
                rt = rt[:fix_bgn_idx] + target + rt[end_index:]
                acc += (len(target) - len(source))
        return rt
