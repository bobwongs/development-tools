//
//  BWFileSystemTool.swift
//  BWiOSDevelopmentToolsSwift
//
//  Created by BobWong on 2017/1/17.
//  Copyright © 2017年 BobWongStudio. All rights reserved.
//

import Foundation

// MARK: File System

/// Whether has directory, if not create one
func hasDirectory(path: String) -> Bool {
    let fileManager = FileManager.default
    if !fileManager.fileExists(atPath: path) {
        do {
            try fileManager.createDirectory(atPath: path, withIntermediateDirectories: true, attributes: nil)
        } catch {
            print("\(path) created failure")
            return false
        }
    }
    
    return true
}

/// Whether has file, if not, create one
func hasFile(path: String) -> Bool {
    let filemanager = FileManager.default
    if !filemanager.fileExists(atPath: path) {
        if !filemanager.createFile(atPath: path, contents: nil, attributes: nil) { return false }
    }
    
    return true
}
