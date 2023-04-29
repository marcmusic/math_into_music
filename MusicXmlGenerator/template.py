def get_xml(musical_sequence = ['C', 'D', 'E', 'F']):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <movement-title>[Music Title - [algorithm code]]</movement-title>
  <identification>
    <creator type="composer">M.A.R.C</creator>
    <creator type="arranger">Math-inspired Music</creator>
    <rights>©M.A.R.C Original Music | [music code]</rights>
    <encoding>
      <software>Finale v25 for Mac</software>
      <encoding-date>2023-04-23</encoding-date>
      <supports attribute="new-system" element="print" type="yes" value="yes"/>
      <supports attribute="new-page" element="print" type="yes" value="yes"/>
      <supports element="accidental" type="yes"/>
      <supports element="beam" type="yes"/>
      <supports element="stem" type="yes"/>
    </encoding>
  </identification>
  <defaults>
    <scaling>
      <millimeters>7.2319</millimeters>
      <tenths>40</tenths>
    </scaling>
    <page-layout>
      <page-height>1545</page-height>
      <page-width>1194</page-width>
      <page-margins type="both">
        <left-margin>140</left-margin>
        <right-margin>70</right-margin>
        <top-margin>70</top-margin>
        <bottom-margin>70</bottom-margin>
      </page-margins>
    </page-layout>
    <system-layout>
      <system-margins>
        <left-margin>0</left-margin>
        <right-margin>0</right-margin>
      </system-margins>
      <system-distance>121</system-distance>
      <top-system-distance>70</top-system-distance>
    </system-layout>
    <appearance>
      <line-width type="stem">0.7487</line-width>
      <line-width type="beam">5</line-width>
      <line-width type="staff">0.7487</line-width>
      <line-width type="light barline">0.7487</line-width>
      <line-width type="heavy barline">5</line-width>
      <line-width type="leger">0.7487</line-width>
      <line-width type="ending">0.7487</line-width>
      <line-width type="wedge">0.7487</line-width>
      <line-width type="enclosure">0.7487</line-width>
      <line-width type="tuplet bracket">0.7487</line-width>
      <note-size type="grace">60</note-size>
      <note-size type="cue">60</note-size>
      <distance type="hyphen">120</distance>
      <distance type="beam">8</distance>
    </appearance>
    <music-font font-family="Maestro,engraved" font-size="20.5"/>
    <word-font font-family="Times New Roman" font-size="10.25"/>
  </defaults>
  <credit page="1">
    <credit-type>title</credit-type>
    <credit-words default-x="140" default-y="1475" font-size="24" valign="top">[Music Title - [algorithm code]]</credit-words>
  </credit>
  <credit page="1">
    <credit-type>composer</credit-type>
    <credit-words default-x="1122" default-y="1407" font-size="12" justify="right" valign="top">M.A.R.C</credit-words>
  </credit>
  <credit page="1">
    <credit-type>rights</credit-type>
    <credit-words default-x="632" default-y="53" font-size="10" justify="center" valign="bottom">©M.A.R.C Original Music | [music code]</credit-words>
  </credit>
  <credit page="1">
    <credit-type>arranger</credit-type>
    <credit-words default-x="1122" default-y="1372" font-size="12" justify="right" valign="top">Math-inspired Music</credit-words>
  </credit>
  <credit page="1">
    <credit-type>subtitle</credit-type>
    <credit-words default-x="140" default-y="1411" font-size="18" valign="top" xml:space="preserve">Based on the [n] Sequence
sequence_and_notes)</credit-words>
  </credit>
  <part-list>
    <score-part id="P1">
      <part-name print-object="no">MusicXML Part</part-name>
      <score-instrument id="P1-I1">
        <instrument-name>ARIA Player</instrument-name>
        <virtual-instrument/>
      </score-instrument>
      <midi-device>ARIA Player</midi-device>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>1</midi-program>
        <volume>80</volume>
        <pan>0</pan>
      </midi-instrument>
    </score-part>
  </part-list>
  <!--=========================================================-->
  <part id="P1">
    {get_notes_code(musical_sequence)}
  </part>
  <!--=========================================================-->
</score-partwise>
    """

def get_notes_code(musical_sequence):
    num_of_notes = len(musical_sequence)
    num_of_measures = (num_of_notes // 4) + 1

    code = ""
    for measure_number in range(1, num_of_measures):
        code += get_measure_code(musical_sequence[:4], measure_number)
        del musical_sequence[:4]

    return code


def get_measure_code(musical_sequence, measure_number):
    code = ""

    if measure_number == 1:
        code+= """<measure number="1" width="242">
        <print>
            <system-layout>
            <system-margins>
                <left-margin>70</left-margin>
                <right-margin>0</right-margin>
            </system-margins>
            <top-system-distance>177</top-system-distance>
            </system-layout>
            <measure-numbering>system</measure-numbering>
        </print>
        <attributes>
            <divisions>2</divisions>
            <key>
            <fifths>0</fifths>
            <mode>major</mode>
            </key>
            <time>
            <beats>4</beats>
            <beat-type>4</beat-type>
            </time>
            <clef>
            <sign>G</sign>
            <line>2</line>
            </clef>
        </attributes>
        <sound tempo="120"/>
        """
    else:
        code+= '<measure number="'+str(measure_number)+'" width="169">'
        if measure_number % 5 == 0:
            code += """<print new-system="yes">
        <system-layout>
          <system-distance>114</system-distance>
        </system-layout>
      </print>
            """

    for note in musical_sequence:
        accidental = ''
        has_accidental = note[-1] == '#'
        
        if has_accidental:
            accidental = note[-1]
            note = note[:-1]

        code += """<note>
        <pitch>
          <step>"""+note+"""</step>
          """+get_alter_code(accidental)+"""
          <octave>4</octave>
        </pitch>
        <duration>2</duration>
        <voice>1</voice>
        <type>quarter</type>
        """+get_accidental_code(accidental)+"""
        <stem>up</stem>
      </note>
        """

    code += """</measure>
    <!--=======================================================-->"""

    return code

def get_accidental_code(accidental_type = ''):
    code = ""
    if accidental_type == '#':
        code +="<accidental>sharp</accidental>"
    if accidental_type == 'b':
        code +="<accidental>flat</accidental>"
    return code

def get_alter_code(accidental_type = ''):
    code = ""
    if accidental_type == '#':
        code +="<alter>1</alter>"
    if accidental_type == 'b':
        code +="<alter>-1</alter>"
    
    return code