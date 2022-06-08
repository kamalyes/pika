import 'ace-builds/src-noconflict/ace'; // mysql模式的包
import 'ace-builds/src-noconflict/mode-python'; // pg模式包
import React from 'react';
import PikaAceEditor from "@/components/CodeEditor/AceEditor/index";

export default function PythonAceEditor(props) {
  return <PikaAceEditor {...props} langugae="python"/>;
}

