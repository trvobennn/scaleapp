"""
Simple program that produces chromatic sequence based on tonic, or additionally scales based on intervals

Includes unit test
"""

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.reference_list = {'flat': ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab'],
                               'sharp': ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']}
        self.flat = ['F','Bb','Eb','Ab','Db','Gb','d','g','c','f','bb','eb']
        self.sharp = ['G','D','A','a','E','B','C','F#','e','b','f#','c#','g#','d#']
        self.is_flat = False
        self.is_sharp = False
        if self.tonic in self.flat:
            self.is_flat = True
        if self.tonic in self.sharp:
            self.is_sharp = True
        self.correct_tonic = self.corrected_()
    def chromatic(self):
        chromatic_list = []
        if self.is_sharp:
            tonic_ind = self.reference_list['sharp'].index(self.correct_tonic)
            for ind in range(tonic_ind, tonic_ind+12):
                if ind < 12:
                    chromatic_list.append(self.reference_list['sharp'][ind])
                if ind >= 12:
                    chromatic_list.append(self.reference_list['sharp'][ind-12])

        elif self.is_flat:
            tonic_ind = self.reference_list['flat'].index(self.correct_tonic)
            for ind in range(tonic_ind, tonic_ind + 12):
                if ind < 12:
                    chromatic_list.append(self.reference_list['flat'][ind])
                if ind >= 12:
                    chromatic_list.append(self.reference_list['flat'][ind - 12])

        return chromatic_list
    def interval(self, intervals):
        # this method is only valid for regular scales, i.e. diatonic or pentatonic
        self.chrm_l = self.chromatic()
        self.interv_list = self.chrm_l.copy()
        for ind, note in enumerate(intervals):
            tonic = self.interv_list[0]

            if note == 'm':
                pass
            if note == 'M':
                self.interv_list.pop(ind+1)
            if note == 'A':
                self.interv_list.pop(ind+1)
                self.interv_list.pop(ind+1)
            if ind == len(intervals) - 1:

                self.interv_list.append(tonic)
        return self.interv_list
    def corrected_(self):

        if len(self.tonic) < 2:
            if self.tonic.islower():
                return self.tonic.upper()
            else:
                return self.tonic
        if len(self.tonic) == 2:
            if self.tonic[0].islower():
                return '%s%s' % (self.tonic[0].upper(), self.tonic[1])
            else:
                return self.tonic



import unittest

class Scale_test(unittest.TestCase):
    def test_a_chromatic(self):
        scale_find = Scale('A')
        self.assertEqual(scale_find.chromatic(),['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'])

    def test_csharp_chromatic(self):
        scale_find = Scale('c#')
        self.assertEqual(scale_find.chromatic(), ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C'])

    def test_eb_chromatic(self):
        scale_find = Scale('Eb')
        self.assertEqual(scale_find.chromatic(), ['Eb','E','F','Gb','G','Ab','A','Bb','B','C','Db','D'])

    def test_a_minor(self):
        scale_find = Scale('a')
        self.assertEqual(scale_find.interval('MmMMmMM'),['A','B','C','D','E','F','G','A'])

    def test_c_major(self):
        scale_find = Scale('C')
        self.assertEqual(scale_find.interval('MMmMMMm'), ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])

    def test_fsharp_major(self):
        scale_find = Scale('F#')
        self.assertEqual(scale_find.interval('MMmMMMm'), ['F#','G#','A#','B','C#','D#','F','F#'])

    def test_e_phrygian(self):
        scale_find = Scale('E')
        self.assertEqual(scale_find.interval('mMMMmMM'), ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E'])

    def test_b_locrian(self):
        scale_find = Scale('B')
        self.assertEqual(scale_find.interval('mMMmMMM'), ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B'])

    def test_f_lydian(self):
        scale_find = Scale('f')
        self.assertEqual(scale_find.interval('MMMmMMm'), ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'])

    def test_fsharp_harmonicminor(self):
        scale_find = Scale('f#')
        self.assertEqual(scale_find.interval('MmMMmAm'), ['F#', 'G#', 'A', 'B', 'C#', 'D', 'F', 'F#'])

    def test_eb_pentatonic(self):
        scale_find = Scale('Eb')
        self.assertEqual(scale_find.interval('MMAMA'), ['Eb', 'F', 'G', 'Bb', 'C', 'Eb'])

    def test_bb_augmented(self):
        scale_find = Scale('Bb')
        self.assertEqual(scale_find.interval('MMMMMM'), ['Bb', 'C', 'D', 'E', 'Gb', 'Ab', 'Bb'])

    def test_d_diminished(self):
        scale_find = Scale('d')
        self.assertEqual(scale_find.interval('AAAA'),['D','F','Ab','B','D',])


if True:
    unittest.main()