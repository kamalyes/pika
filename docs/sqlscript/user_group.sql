/*
Navicat MySQL Data Transfer

Source Server         : 腾讯云
Source Server Version : 50735
Source Host           : localhost:3306
Source Database       : auto_test

Target Server Type    : MYSQL
Target Server Version : 50735
File Encoding         : 65001

Date: 2022-01-20 09:55:38
*/

SET
FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user_group
-- ----------------------------
DROP TABLE IF EXISTS `user_group`;
CREATE TABLE `user_group`
(
    `id`             int(11) NOT NULL AUTO_INCREMENT COMMENT '用户组id',
    `name`           varchar(255) NOT NULL COMMENT '用户组名称',
    `description`    varchar(255)          DEFAULT NULL COMMENT '备注信息',
    `enabled_flag`   int(11) DEFAULT '1' COMMENT '禁用/启用 1：启用、0：禁用',
    `create_user_no` varchar(20)           DEFAULT NULL COMMENT '创建者用户编号',
    `update_user_no` varchar(20)           DEFAULT NULL COMMENT '修改者用户编号',
    `create_date`    datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建日期',
    `update_date`    datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日期',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COMMENT='用户组';

-- ----------------------------
-- Records of user_group
-- ----------------------------
INSERT INTO `user_group`
VALUES ('1', '互动视频', 'string', '1', 'SystemSync', null, '2022-01-21 21:35:06', '2022-01-22 21:36:44');
INSERT INTO `user_group`
VALUES ('2', '互联网医疗', 'string', '1', 'SystemSync', null, '2022-01-21 21:35:10', '2022-01-22 21:36:53');
INSERT INTO `user_group`
VALUES ('3', '研发效能中心', 'string', '1', 'SystemSync', null, '2022-01-21 21:35:11', '2022-01-22 21:37:14');
