//
//  BWAPIManagerGeneratorVC.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2017/1/18.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Cocoa

class BWAPIManagerGeneratorVC: NSViewController {
    // MARK: UI
    // --------------- Source ---------------
    @IBOutlet weak var copyrightTextField: NSTextField!
    @IBOutlet weak var projectTextField: NSTextField!
    @IBOutlet weak var authorTextField: NSTextField!
    @IBOutlet weak var prefixTextField: NSTextField!
    @IBOutlet weak var importFileTextField: NSTextField!
    @IBOutlet weak var basicVCTextField: NSTextField!
    @IBOutlet weak var moduleTextField: NSTextField!
    @IBOutlet weak var sourceScrollView: NSScrollView!
    
    // --------------- Generation ---------------
    @IBOutlet weak var generationScrollView: NSScrollView!
    
    // MARK: View Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Read data from cache
        let userDefaults = UserDefaults.standard
        if let copyRight = userDefaults.value(forKey: kCopyRight) { copyrightTextField.stringValue = copyRight as! String }
        if let project = userDefaults.value(forKey: kProject) { projectTextField.stringValue = project as! String }
        if let author = userDefaults.value(forKey: kAuthor) { authorTextField.stringValue = author as! String }
        if let prefix = userDefaults.value(forKey: kPrefix) { prefixTextField.stringValue = prefix as! String }
        if let importFile = userDefaults.value(forKey: kAPIManagerImportFile) { importFileTextField.stringValue = importFile as! String }
        if let basicVC = userDefaults.value(forKey: kBasicAPIManager) { basicVCTextField.stringValue = basicVC as! String}
        if let module = userDefaults.value(forKey: kAPIManagerModule) { moduleTextField.stringValue = module as! String }
    }
    
    // MARK: Action
    @IBAction func resetAction(_ sender: Any) {
        sourceTextView.string = ""
    }
    
    @IBAction func generateAction(_ sender: Any) {
        // Set the path parameters for source and generation directory
        let source = sourceTextView.string
        let functionDirectoryPath = "\(NSHomeDirectory())/Desktop/Generator/APIManager"
        let sourceDirectoryPath = "\(functionDirectoryPath)/Source"
        let generationDirectoryPath = "\(functionDirectoryPath)/Generation"
        
        let pathSource = "\(sourceDirectoryPath)/source.txt"
        let pathGeneration = "\(generationDirectoryPath)/generation.txt"
        
        // If there not has file, create
        if !hasDirectory(path: sourceDirectoryPath) { return }
        if !hasFile(path: pathSource) { return }
        
        let copyRight = NSString(string: copyrightTextField.stringValue).length > 0 ? copyrightTextField.stringValue : "BobWongStudio"
        let projectName = NSString(string: projectTextField.stringValue).length > 0 ? projectTextField.stringValue : "BWProject"
        let authorName = NSString(string: authorTextField.stringValue).length > 0 ? authorTextField.stringValue : "BobWong"
        let prefixName = NSString(string: prefixTextField.stringValue).length > 0 ? prefixTextField.stringValue : "BW"
        let importFile = NSString(string: importFileTextField.stringValue).length > 0 ? importFileTextField.stringValue : "#import <UIKit/UIKit.h>"
        let basicVC = NSString(string: basicVCTextField.stringValue).length > 0 ? basicVCTextField.stringValue : "UIViewController"
        let moduleName = NSString(string: moduleTextField.stringValue).length > 0 ? moduleTextField.stringValue : "APIManager"
        
        generationTextView.string = executePythonScript(scriptInBundle: "generator_api_mananger", sourcePath: pathSource, generationPath: pathGeneration, source: source, argumentsExceptPath: ["-c", copyRight, "-p", projectName, "-a", authorName, "-P", prefixName, "-i", importFile, "-b", basicVC, "-m", moduleName])
        
        
        // Write data to cache
        let userDefaults = UserDefaults.standard
        userDefaults.setValue(copyRight, forKey: kCopyRight)
        userDefaults.setValue(projectName, forKey: kProject)
        userDefaults.setValue(authorName, forKey: kAuthor)
        userDefaults.setValue(prefixName, forKey: kPrefix)
        userDefaults.setValue(importFile, forKey: kAPIManagerImportFile)
        userDefaults.setValue(basicVC, forKey: kBasicAPIManager)
        userDefaults.setValue(moduleName, forKey: kAPIManagerModule)
    }
    
    // MARK: Getter and Setter
    var sourceTextView: NSTextView {
        get { return sourceScrollView.contentView.documentView as! NSTextView }
    }
    
    var generationTextView: NSTextView {
        get { return generationScrollView.contentView.documentView as! NSTextView }
    }
}
