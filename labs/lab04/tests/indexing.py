test = {
  'name': 'List Indexing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the expression that indexes into x to output the 7
          x[2][1]
          >>> x = [[3, [5, 7], 9]] # Write the expression that indexes into x to output the 7
          x[0][1][1]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4]
          8dfecce35cfbb620490b1aa9637bdafd
          # locked
          >>> lst[3][0]
          89d2c4e2851d68c81d820360eb31bc36
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
