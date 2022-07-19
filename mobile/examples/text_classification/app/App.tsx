import { StatusBar } from 'expo-status-bar';
import AppLoading from 'expo-app-loading'
import { Platform, Alert, Button, StyleSheet, TextInput, View } from 'react-native';
import React, {useState} from 'react'
import * as ort from 'onnxruntime-react-native';
import { Asset } from 'expo-asset';

let myModel: ort.InferenceSession;
let myText = "I love tomatoes"
let modelLoaded=false;

function myAlert(alertTitle: string, alertText: string) {
  console.log(alertTitle + ": " + alertText)
  if (Platform.OS === 'web') {
    alert(alertTitle + " " + alertText)
  } else {
    Alert.alert(alertTitle, alertText)
  }
}

async function loadModel() {
  try {
    const assets = await Asset.loadAsync(require('./assets/distilbert-base-uncased-finetuned-sst-2-english-aug.ort'));
    const modelUri = assets[0].localUri;
    if (!modelUri) {
      myAlert('failed to get model URI', `${assets[0]}`);
    } else {
      myModel = await ort.InferenceSession.create(modelUri);
      myAlert(
        'model loaded successfully',
        `input names: ${myModel.inputNames}, output names: ${myModel.outputNames}`);
      modelLoaded=true
    }
  } catch (e) {
    myAlert('failed to load model', `${e}`);
    throw e;
  }
}

async function onChangeText(text: string) {
    console.log(text)
    myText = text
}

async function runModel() {
  try {
    const inputData = [myText];
    const feeds:Record<string, ort.Tensor> = {};
    feeds[myModel.inputNames[0]] = new ort.Tensor(inputData, [inputData.length]);
    console.log(feeds);
    const fetches = await myModel.run(feeds);
    console.log(fetches);
    const output = fetches[myModel.outputNames[0]];
    if (!output) {
      myAlert('failed to get output', `${myModel.outputNames[0]}`);
    } else {
      myAlert(
        'model inference successfully',
        `output shape: ${output.dims}, output data: ${output.data}`);
    }
  } catch (e) {
    myAlert('failed to inference model', `${e}`);
    throw e;
  }
}

function setModelLoaded(state: boolean) {
  modelLoaded = state;
}

function loadModelError() {
  modelLoaded=false;
  myAlert("Model error:", "Could not load model");
}

export default function App() {
  const [modelLoaded, setModelLoaded] = useState(false)
  const [myText, onChangeText] = useState("I love tomatoes")

  if (!modelLoaded) {
    return (
      <AppLoading      
      startAsync={loadModel}
      onFinish={() => setModelLoaded(true)}
      onError={() => loadModelError()}
      />
    );
  } else {
    return (
      <View style={styles.container}>
        <TextInput onChangeText={onChangeText} value={myText}></TextInput>
        <Button title='Classify' onPress={runModel}></Button>
        <StatusBar style="auto" />
      </View>
  );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
