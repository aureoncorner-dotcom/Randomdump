This directory preserves an initial implementation run, not final benchmark results.

The initial parser incorrectly required exactly six clues, leaving 13 seven-clue questions unresolved. Its raw-error accounting also incorrectly treated parse failures as model errors; its enumeration count included unparsed questions. These were assistant-side implementation errors, corrected before the final report. The initial summary must not be cited as the model's raw performance.

The final parser accepts nonempty clue lists, still requiring every clause to match an explicit supported template. Final raw scoring reads the original prediction independently of parser success. Final enumeration counts parsed questions only. No source question, prediction, or published target was changed. The corrected run covers the same complete 250 records.
