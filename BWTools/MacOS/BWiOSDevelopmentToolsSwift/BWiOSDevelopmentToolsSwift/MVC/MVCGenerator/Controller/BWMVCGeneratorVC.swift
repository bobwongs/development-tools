//
//  BWMVCGeneratorVC.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 17/1/13.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWMVCGeneratorVC: NSViewController {
    
    // MARK: UI
    // --------------- Source ---------------
    @IBOutlet weak var tfCopyRight: NSTextField!
    @IBOutlet weak var tfProject: NSTextField!
    @IBOutlet weak var tfAuthor: NSTextField!
    @IBOutlet weak var tfPrefix: NSTextField!
    @IBOutlet weak var tfImportFile: NSTextField!
    @IBOutlet weak var tfBasicVC: NSTextField!
    @IBOutlet weak var tfModule: NSTextField!
    @IBOutlet weak var svProperty: NSScrollView!
    
    // --------------- Generation ---------------
    @IBOutlet weak var svGeneration: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Read data from cache
        let userDefaults = UserDefaults.standard
        if let copyRight = userDefaults.value(forKey: kCopyRight) { tfCopyRight.stringValue = copyRight as! String }
        if let project = userDefaults.value(forKey: kProject) { tfProject.stringValue = project as! String }
        if let author = userDefaults.value(forKey: kAuthor) { tfAuthor.stringValue = author as! String }
        if let prefix = userDefaults.value(forKey: kPrefix) { tfPrefix.stringValue = prefix as! String }
        if let importFile = userDefaults.value(forKey: kImportFile) { tfImportFile.stringValue = importFile as! String }
        if let basicVC = userDefaults.value(forKey: kBasicVC) { tfBasicVC.stringValue = basicVC as! String}
        if let module = userDefaults.value(forKey: kModule) { tfModule.stringValue = module as! String }
    }
    
    // MARK: Action
    @IBAction func btnActionReset(_ sender: Any) {
        tvMVCSource.string = ""
    }
    
    @IBAction func btnActionGenerate(_ sender: Any)
    {
        // Set the path parameters for source and generation directory
        let source = tvMVCSource.string
        let pathMVCDir = "\(NSHomeDirectory())/Desktop/Generator/MVC"
        let pathSourceDir = "\(pathMVCDir)/Source"
        let pathGenerationDir = "\(pathMVCDir)/Generation"
        
        let pathSource = "\(pathSourceDir)/source.txt"
        let pathGeneration = "\(pathGenerationDir)/generation.txt"
        
        // If there not has file, create
        if !hasDirectory(path: pathSourceDir) { return }
        if !hasFile(path: pathSource) { return }
        
        let copyRight = NSString(string: tfCopyRight.stringValue).length > 0 ? tfCopyRight.stringValue : "BobWongStudio"
        let projectName = NSString(string: tfProject.stringValue).length > 0 ? tfProject.stringValue : "BWProject"
        let authorName = NSString(string: tfAuthor.stringValue).length > 0 ? tfAuthor.stringValue : "BobWong"
        let prefixName = NSString(string: tfPrefix.stringValue).length > 0 ? tfPrefix.stringValue : "BW"
        let importFile = NSString(string: tfImportFile.stringValue).length > 0 ? tfImportFile.stringValue : "#import <UIKit/UIKit.h>"
        let basicVC = NSString(string: tfBasicVC.stringValue).length > 0 ? tfBasicVC.stringValue : "UIViewController"
        let moduleName = NSString(string: tfModule.stringValue).length > 0 ? tfModule.stringValue : "MVC"
        
        tvGeneration.string = executePythonScript(scriptInBundle: "generator_mvc", sourcePath: pathSource, generationPath: pathGeneration, source: source, argumentsExceptPath: ["-c", copyRight, "-p", projectName, "-a", authorName, "-P", prefixName, "-i", importFile, "-b", basicVC, "-m", moduleName]) ?? ""
        
        
        // Write data to cache
        let userDefaults = UserDefaults.standard
        userDefaults.setValue(copyRight, forKey: kCopyRight)
        userDefaults.setValue(projectName, forKey: kProject)
        userDefaults.setValue(authorName, forKey: kAuthor)
        userDefaults.setValue(prefixName, forKey: kPrefix)
        userDefaults.setValue(importFile, forKey: kImportFile)
        userDefaults.setValue(basicVC, forKey: kBasicVC)
        userDefaults.setValue(moduleName, forKey: kModule)
    }
    
    // MARK: Getter and Setter
    var tvMVCSource: NSTextView {
        get { return svProperty.contentView.documentView as! NSTextView }
    }
    
    var tvGeneration: NSTextView {
        get { return svGeneration.contentView.documentView as! NSTextView }
    }
    
}

/*
 Mac OS Developmemt Study
    // 可以拼接在文件后头
    let fileHandleSource = FileHandle.init(forWritingAtPath: pathSource)
    fileHandleSource?.seekToEndOfFile()
    fileHandleSource?.write((source?.data(using: String.Encoding.utf8))!)
    fileHandleSource?.closeFile()
 */
