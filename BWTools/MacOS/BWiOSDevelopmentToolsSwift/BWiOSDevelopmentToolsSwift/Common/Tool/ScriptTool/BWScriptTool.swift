//
//  BWScriptTool.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2017/1/17.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Foundation

// MARK: Execute Script

/// Execute python script
/// - Parameter scriptInBundle: Python script file name in main bundle
func executePythonScript(scriptInBundle: String, sourcePath: String, generationPath: String, source: String?, argumentsExceptPath: [String]?) -> String?
{
    guard let path = Bundle.main.path(forResource: scriptInBundle, ofType: "py") else {
        print("no \(scriptInBundle).py file")
        return nil
    }
    
    var arguments = argumentsExceptPath
    arguments?.insert(path, at: 0)
    return executeScript(scriptPath: path, sourcePath: sourcePath, generationPath: generationPath, source: source, launchPath: "/usr/bin/python", arguments: arguments)
}

/// Execute script
func executeScript(scriptPath: String, sourcePath: String, generationPath: String, source: String?, launchPath: String, arguments: [String]?) -> String? {
    do {
        try source?.write(toFile: sourcePath, atomically: false, encoding: String.Encoding.utf8)  // Replace all content in source file
    }
    catch {
        print("MVC Source Write Error!")
        return nil;
    }
    
    // ------------ Execute python script ------------
    let task = Process()
    task.launchPath = launchPath
    task.arguments = arguments
    let outputPipe = Pipe()
    task.standardInput = Pipe()
    task.standardOutput = outputPipe
    task.launch()
    task.waitUntilExit()
    
    let fileHandle = outputPipe.fileHandleForReading
    let output = NSString.init(data: fileHandle.readDataToEndOfFile(), encoding: String.Encoding.utf8.rawValue)
    print("Output is \(output)")
    
    
    // ------------ Write the result ------------
    do {
        let stringGeneration = try NSString.init(contentsOfFile: generationPath, encoding: String.Encoding.utf8.rawValue) as String
        return stringGeneration
    } catch { print("no stringGeneration")}
    
    return nil
}
