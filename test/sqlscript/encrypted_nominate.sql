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

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for encrypted_nominate
-- ----------------------------
DROP TABLE IF EXISTS `encrypted_nominate`;
CREATE TABLE `encrypted_nominate` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '序号',
  `question` varchar(255) DEFAULT NULL COMMENT '密保问题',
  `create_user_no` varchar(20) DEFAULT '' COMMENT '创建者用户编号',
  `update_user_no` varchar(20) DEFAULT '' COMMENT '修改者用户编号',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COMMENT='密保推荐';

-- ----------------------------
-- Records of encrypted_nominate
-- ----------------------------
INSERT INTO `encrypted_nominate` VALUES ('1', '您母亲的姓名是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:59', '2022-01-20 09:25:52');
INSERT INTO `encrypted_nominate` VALUES ('2', '您父亲的姓名是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:59', '2022-01-20 09:25:52');
INSERT INTO `encrypted_nominate` VALUES ('3', '您配偶的姓名是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:35', '2022-01-20 09:25:52');
INSERT INTO `encrypted_nominate` VALUES ('5', '您的出生地是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:35', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('6', '您高中班主任的名字是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:35', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('7', '您初中班主任的名字是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:35', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('8', '您小学班主任的名字是？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:35', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('9', '您的狗狗是什么品种？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('10', '为什么我们不吃生马铃薯？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('11', '为什么鸡会吃沙粒？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('12', '为什么不要空腹喝牛奶？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('13', '信鸽千里返航的秘密是什么？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('15', '鹰眼为什么特别敏锐？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
INSERT INTO `encrypted_nominate` VALUES ('16', '太阳为什么是圆的？', 'SystemSync', 'SystemSync', '2022-01-20 09:25:36', '2022-01-20 09:25:53');
